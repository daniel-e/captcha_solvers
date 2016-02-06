#!/usr/bin/env python3

from tools.image import read_rgb_image, write_rgb_image
import argparse
import numpy as np
from skimage import io

p = argparse.ArgumentParser(description = 'Extract an image from a 9x9 reCAPTCHA image.')
p.add_argument('-i', help = 'input image', required = True)
p.add_argument('-y', help = 'row', required = True, type = int)
p.add_argument('-x', help = 'column', required = True, type = int)
p.add_argument('-o', help = 'output image', default = None)
p.add_argument('-v', help = 'show output image', default = False, action = 'store_true')
args = p.parse_args()

def read_image(fname, row, col):
	i = read_rgb_image(fname)
	assert(i.shape[0] == 300)
	assert(i.shape[1] == 300)
	i = i[row * 100:row * 100 + 100, col * 100:col * 100 + 100]
	return i

i = read_image(args.i, args.y, args.x)

if args.o != None:
	write_rgb_image(args.o, i)

if args.v:
	io.imshow(i)
