import cv2
import numpy as np
from matplotlib import pyplot as plt

import json

dir = "docs/2_3"

with open(dir + "/config.json") as f:
    df = json.load(f)

keys = list(df.keys())

key1 = keys[0]
key2 = keys[1]

img = cv2.imread(dir + "/" + key1)

img2 = cv2.imread(dir + "/" + key2 + '_resized.jpeg')

orgHeight, orgWidth = img.shape[:2]
orgHeight2, orgWidth2 = img2.shape[:2]

width1 = df[key1]["width"]
width2 = df[key2]["width"]

r = width1 / width2

x = int(df[key2]["ow"] * r) - df[key1]["ow"]
y = int(df[key2]["oh"] * r) - df[key1]["oh"]

h = orgHeight
w = orgWidth

print(x, y, h, w)

# img[top : bottom, left : right]
# サンプル1の切り出し、保存
img_trim = img2[y : y + h, x: x + w]
cv2.imwrite(dir + "/" + key2 + '_trim.jpeg', img_trim)