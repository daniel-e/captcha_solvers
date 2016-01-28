#!/usr/bin/env python

import cv2, argparse
import numpy as np

p = argparse.ArgumentParser()
p.add_argument('-i', required = True)
p.add_argument('-y', required = True, type = int)
p.add_argument('-x', required = True, type = int)
p.add_argument('-o', default = None)
p.add_argument('-v', default = False, action = 'store_true')
args = p.parse_args()

def read_image(fname, row, col):
	i = cv2.imread(fname)
	i = i[row * 100:row * 100 + 100, col * 100:col * 100 + 100]
	i = cv2.resize(i, (64, 64))
	return i

i = read_image(args.i, args.y, args.x)

if args.o != None:
	cv2.imwrite(args.o, i)

if args.v:
	cv2.imshow('image', i)
	cv2.waitKey(0)


