from requests import exceptions
import argparse
import cv2
import os
import requests

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True,
                help="search query to search Bing Image API for")
ap.add_argument("-o", "--output", required=True,
                help="path to output directory of images")
args = vars(ap.parse_args())

API_KEY = "83c857b342ca4a39814ce9dbed2f6f53"
MAX_RESULTS = 50
GROUP_SIZE = 5

URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search/"

EXCEPTIONS = set([IOError, FileNotFoundError, exceptions.RequestException,
                  exceptions.HTTPError, exceptions.ConnectionError, exceptions.Timeout])

term = args["query"]
headers = {"Ocp-Apim-Subscription-Key": API_KEY}
params = {"q": term, "offset": 0, "count": GROUP_SIZE}

# make the search
print("[INFO] searching Bing API for '{}'".format(term))
search = requests.get(URL, headers=headers, params=params)
search.raise_for_status()

# grab the results from the search, including the total number of
# estimated results returned by the Bing API

results = search.json()
estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
print("[INFO] {} total results for '{}'".format(estNumResults, term))

total = 0

for offset in range(0, estNumResults, GROUP_SIZE):
    print("[INFO] making request for group {}-{} of {}...".format(offset,
                                                                  offset + GROUP_SIZE, estNumResults))
    params["offset"] = offset
    search = requests.get(URL, headers=headers, params=params)
    search.raise_for_status()
    results = search.json()
    print("[INFO] saving images for group {}-{} of {}...".format(offset,
                                                                 offset + GROUP_SIZE, estNumResults))

    for v in results["value"]:
        try:
            print("[INFO] fetching: {}".format(v["contentUrl"]))
            r = requests.get(v["contentUrl"], timeout=30)
            ext = v["contentUrl"][v["contentUrl"].rfind("."):]
            p = os.path.sep.join(
                [args["output"], "{}{}".format(str(total).zfill(8), ext)])

            f = open(p, "wb")
            f.write(r.content)
            f.close()

        except Exception as e:
            if type(e) in EXCEPTIONS:
                print("[INFO] skipping: {}".format(v["contentUrl"]))
                continue

        # loading images using opncv
        image = cv2.imread(p)
        if image is None:
            print("[INFO] deleting: {}".format(p))
            os.remove(p)
            continue

        total += 1