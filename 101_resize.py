import cv2
import numpy as np
from matplotlib import pyplot as plt
import json

dir = "docs/2_1"

with open(dir + "/config.json") as f:
    df = json.load(f)

keys = list(df.keys())

key1 = keys[0]
key2 = keys[1]

print(key1, key2)

img = cv2.imread(dir + "/" + key2)

orgHeight, orgWidth = img.shape[:2]

print("height", orgHeight, "width", orgWidth)

width1 = df[key1]["width"]
width2 = df[key2]["width"]

r = width1 / width2

print(r)

newHeight = int(orgHeight * r)
newWidth = int(orgWidth * r)

print("height", newHeight, "width", newWidth)

resized = cv2.resize(img, (newWidth, newHeight))

cv2.imwrite(dir + "/" + key2 + '_resized.jpeg', resized)