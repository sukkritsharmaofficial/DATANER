<p align="center"><img width=45% src="https://raw.githubusercontent.com/sukkritsharmaofficial/DATANER/master/media/dataner.png"></p>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Basic Overview

Automatic dataset generating tool using Computer Vision API’s for enhancing and enriching your datasets.

<p align="center"><img width=60% src="https://raw.githubusercontent.com/sukkritsharmaofficial/DATANER/master/media/Folders.png"></p>

## Latest Development Changes
```bash
git clone https://github.com/sukkritsharmaofficial/DATANER.git
```

## Download Dependencies
```bash
pip install opencv-python
pip install Pillow
```

## Code

Importing Dependencies

```python
from requests import exceptions
import argparse
import cv2
import os
import requests
```
## Retrieve API key
<br>

Step 1: Go to the [Microsoft Azure Cognitive Services Marketplace](https://azure.microsoft.com/en-us/try/cognitive-services/).

Step 2: Click on the "Search APIs" tab and then on the "Get API Key" button:

Step 3: On the next screen, agree to Microsoft's TOS, select your country and click the "Next" button:

Step 4: If you are asked to login, please login to your Microsoft account.

Step 5: Visit your [Microsoft APIs page](https://azure.microsoft.com/en-us/try/cognitive-services/my-apis/) and scroll down to find "Key 1".

Step 6 : Copy the API Key and Paste where mentioned "ENTER YOUR API KEY HERE".

<br>

## Changable settings and paths
Paste your API Key and Change number of results and download group size.
<br></br>
```python
API_KEY = "ENTER YOUR API KEY HERE"
MAX_RESULTS = 50
GROUP_SIZE = 5
```

## How to run
```bash
python launch_api.py --query [ENTER YOUR QUERY HERE] --output [PATH FOR OUTPUT FOLDER]
```
Output
<p align="center"><img width=60% src="https://raw.githubusercontent.com/sukkritsharmaofficial/DATANER/master/media/Charmandar.png"></p>
