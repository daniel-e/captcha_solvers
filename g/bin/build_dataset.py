#!/usr/bin/env python3

from tools.sliding import normed_windows
from tools.image import read_rgb_image, flatten
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
	for i in normed_windows(read_rgb_image(fn), [1.0, 0.5]):
		d = flatten(i)
		f.write(",".join([str(k) for k in d]) + "\n")
		l.write(str(c) + "\n")

m = open(os.path.join(args.o, args.labelmapping), "w")
for k, v in mapping.items():
	m.write(k + " " + str(v) + "\n")
