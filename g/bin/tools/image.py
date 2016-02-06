#!/usr/bin/env python3

from skimage import io
from skimage.transform import resize
import numpy as np
import unittest

def read_rgb_image(fname):
	i = io.imread(fname)
	check_img(i)
	return i

def write_rgb_image(fname, img):
	check_img(img)
	io.imsave(fname, img)

def resize_rgb_image(img, siz):
	assert(False)
	check_img(img)
	return resize(img, size) * 255

def flatten(img):
	check_img(img)
	r = img[:, :, 0].flatten(order = 'F')
	g = img[:, :, 1].flatten(order = 'F')
	b = img[:, :, 2].flatten(order = 'F')
	return np.append(np.append(r, g), b)

def unflatten(arr, h, w):
	r = arr[:h*w]
	g = arr[h*w:2*h*w]
	b = arr[2*h*w:]
	z = np.zeros((h, w, 3), np.uint8)
	z[:, :, 0] = np.reshape(r, (h, w), order = 'F').copy()
	z[:, :, 1] = np.reshape(g, (h, w), order = 'F').copy()
	z[:, :, 2] = np.reshape(b, (h, w), order = 'F').copy()
	check_img(z)
	return z

# -----------------------------------------------------------------------------
# internal functions
# -----------------------------------------------------------------------------

def check_img(i):
	assert(len(i.shape) == 3)
	assert(i.shape[2] == 3)
	assert(i.dtype == 'uint8')

class TestFunctions(unittest.TestCase):
	def test_flatten(self):
		a = np.array([[1,2], [3,4]])
		b = np.array([[5,6], [7,8]])
		c = np.array([[9,10], [11,12]])
		i = np.zeros((2, 2, 3), np.uint8)
		i[:, :, 0] = a
		i[:, :, 1] = b
		i[:, :, 2] = c
		f = list(flatten(i))
		self.assertEqual(f, [1,3,2,4,5,7,6,8,9,11,10,12])
		x = unflatten(f, 2, 2)
		self.assertTrue(np.equal(i, x).all())

if __name__ == '__main__':
	unittest.main()
