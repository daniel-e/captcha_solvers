#!/usr/bin/env python3

from tools.sliding import normed_windows
from tools.image import read_rgb_image, flatten, resize_rgb_image
import argparse, os

p = argparse.ArgumentParser()
p.add_argument('-i', help = 'Image path.', required = True)
p.add_argument('-o', help = 'Output directory.', required = True)
p.add_argument('--labels', default = "labels.txt")
p.add_argument('--features', default = "features.txt")
p.add_argument('--labelmapping', default = "map.txt")
args = p.parse_args()

def labels_and_files():
	for i in os.listdir(args.i):
		for j in os.listdir(os.path.join(args.i, i)):
			yield (i, os.path.join(args.i, i, j))

if not os.path.exists(args.o):
	os.makedirs(args.o)

f = open(os.path.join(args.o, args.features), "w")
l = open(os.path.join(args.o, args.labels), "w")

mapping = {}
for lb, fn in labels_and_files():
	if not lb in mapping:
		mapping[lb] = len(mapping)
	c = mapping[lb]
	print (c, lb, fn)
	img = resize_rgb_image(read_rgb_image(fn), (32, 32))
	for i in normed_windows(img, [1.0]):
		d = flatten(i)
		f.write(",".join([str(k) for k in d]) + "\n")
		l.write(str(c) + "\n")

m = open(os.path.join(args.o, args.labelmapping), "w")
for k, v in mapping.items():
	m.write(k + " " + str(v) + "\n")
