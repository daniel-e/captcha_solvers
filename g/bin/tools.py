import cv2
import numpy as np

def swap_colors(img): # cv2 uses BGR
	check_img(img)
	i = img.copy()
	b = i[:, :, 0]
	r = i[:, :, 2]
	i[:, :, 0], i[:, :, 2] = r.copy(), b.copy()
	return i

def check_img(i):
	assert(len(i.shape) == 3)
	assert(i.shape[2] == 3)
	assert(i.dtype == 'uint8')
	
def read_rgb_image(fname):
	i = swap_colors(np.uint8(cv2.imread(fname)))  # BGR
	check_img(i)
	return i

def write_rgb_image(fname, img):
	i = img.copy()
	check_img(i)
	cv2.imwrite(fname, swap_colors(i))

def resize_rgb_image(img, siz):
	check_img(img)
	return swap_colors(cv2.resize(swap_colors(img), siz))
