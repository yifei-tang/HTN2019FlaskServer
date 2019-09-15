import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys
from io import BytesIO
import re
def setUpKey():
    # Add your Computer Vision subscription key and endpoint to your environment variables.
    subscription_key = 'e26e9d900bcb477ebb72985ededb6215'
    endpoint = 'http://westus2.api.cognitive.microsoft.com/'
    analyze_url = endpoint + "vision/v1.0/ocr"

    # Set image_path to the local path of an image that you want to analyze.
    image_path = "/home/yifei/Downloads/rec.jpg"

    # Read the image into a byte array/
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json() #returns a dictionary so you can access elements by the key
    return analysis 