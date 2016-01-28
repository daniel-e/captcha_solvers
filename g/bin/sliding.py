#!/usr/bin/env python

from tools import read_rgb_image, swap_colors, resize_rgb_image
import argparse, math, cv2
import numpy as np

p = argparse.ArgumentParser()
p.add_argument('-i', required = True)
p.add_argument('-o', required = True)
args = p.parse_args()

min_window_size = 22
out_img_size = 32
window_sizes = [0.5, 0.38, 0.25]


def win_sizes(img, p):
	m = min(img.shape[0], img.shape[1])
	return [j for j in [math.trunc(m * i) for i in p] if j >= min_window_size]

def win_positions(img, window_sizes):
	for ws in window_sizes:
		for y in range(0, img.shape[0] - ws + 1, ws / 2):
			for x in range(0, img.shape[1] - ws + 1, ws / 2):
				yield (ws, y, x)

def sub_images(img, positions):
	for p in positions:
		yield img[p[1]:p[1]+p[0] - 1, p[2]:p[2]+p[0]-1]

def resize_images(images):
	return [resize_rgb_image(i, (out_img_size, out_img_size)) for i in images]


src = read_rgb_image(args.i)

sizes = win_sizes(src, window_sizes)

pos = win_positions(src, sizes)

res = resize_images(sub_images(src, pos))

for i in res:
	cv2.imshow('b', swap_colors(i))
	cv2.waitKey(0)
