#!/usr/bin/env python3

from tools.image import read_rgb_image, resize_rgb_image, flatten
import argparse, os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

p = argparse.ArgumentParser()
p.add_argument('-i', help = 'Input image.', required = True)
p.add_argument('-d', help = 'Dataset path.', required = True)
p.add_argument('--labels', default = "labels.txt")
p.add_argument('--features', default = "features.txt")
p.add_argument('--labelmapping', default = "map.txt")
p.add_argument('-k', default = 7, type = int)
args = p.parse_args()

print ("Loading model ...")
data = np.loadtxt(os.path.join(args.d, args.features), delimiter = ',') / 255
labels = np.loadtxt(os.path.join(args.d, args.labels))
lines = [i.strip().split(" ") for i in open(os.path.join(args.d, args.labelmapping))]
labelmap = dict([(int(n), l) for l, n in lines])

clf = KNeighborsClassifier(n_neighbors = 7, algorithm = 'brute')
clf.fit(data, labels.ravel())

# load query image, resize to 32x32 and scale to [0, 1]
img = resize_rgb_image(read_rgb_image(args.i), (32, 32))
arr = flatten(img) / 255
arr = np.reshape(arr, (1, -1))
t = clf.predict(arr)
print (labelmap[int(t[0])])
