#!/usr/bin/env python3

from tools.image import read_rgb_image, resize_rgb_image, flatten, write_rgb_image
from tools.sliding import normed_windows
import argparse, os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

p = argparse.ArgumentParser()
p.add_argument('-i', help = 'Input image.', required = True)
p.add_argument('-d', help = 'Dataset path.', required = True)
p.add_argument('--labels', default = "labels.txt")
p.add_argument('--features', default = "features.txt")
p.add_argument('--labelmapping', default = "map.txt")
p.add_argument('-o', help = 'Image with boxes', required = True)
p.add_argument('-k', default = 7, type = int)
args = p.parse_args()

def box(arr, y, x, d):
    i = arr.copy()
    for py in range(y, y + d):
        i[py, x, 0] = 255
        i[py, x + d - 1, 0] = 255
    for px in range(x, x + d):
        i[y, px, 0] = 255
        i[y + d - 1, px, 0] = 255
    return i

print ("Loading model ...")
data = np.loadtxt(os.path.join(args.d, args.features), delimiter = ',') / 255
labels = np.loadtxt(os.path.join(args.d, args.labels), np.uint8)
lines = [i.strip().split(" ") for i in open(os.path.join(args.d, args.labelmapping))]
labelmap = dict([(int(n), l) for l, n in lines])

clf = KNeighborsClassifier(n_neighbors = 7, algorithm = 'brute')
clf.fit(data, labels)

img = resize_rgb_image(read_rgb_image(args.i), (32, 32))
d = []
for i, details in normed_windows(img, [1.0], details = True):
    arr = flatten(i) / 255
    arr = np.reshape(arr, (1, -1))
    t = clf.predict(arr)
    c = t[0]
    print (c, labelmap[c])
    distances, idx = clf.kneighbors(arr)
    distances = [d for d, p in zip(distances.flatten(), idx.flatten()) if labels[p] == c]
    s = sum(distances) / len(distances)
    d.append([s, c, details])

d = sorted(d)
for s, c, details in d[:3]:
    print (s, labelmap[c], details)
    img = box(img, details[1], details[2], details[0])

write_rgb_image(args.o, img)
