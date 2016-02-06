#!/usr/bin/env python3

import unittest, math
import numpy as np
from skimage.transform import resize

def normed_windows(arr, p = [0.5, 0.38, 0.25], d = 32):
    sizes = win_sizes(arr, p)
    pos = win_positions(arr, sizes)
    return (np.uint8(resize(i, (d, d)) * 255) for i in sub_images(arr, pos))

# -----------------------------------------------------------------------------
# internal functions
# -----------------------------------------------------------------------------

def win_sizes(arr, p, min_window_size = 22):
	m = min(arr.shape[0], arr.shape[1])
	return [j for j in [math.trunc(m * i) for i in p] if j >= min_window_size]

def win_positions(img, window_sizes):
	for ws in window_sizes:
		for y in range(0, img.shape[0] - ws + 1, int(ws / 2)):
			for x in range(0, img.shape[1] - ws + 1, int(ws / 2)):
				yield (ws, y, x)

def sub_images(img, positions):
    for p in positions:
        w = p[0]
        y = p[1]
        x = p[2]
        yield img[y:y + w, x:x + w]

class TestFunctions(unittest.TestCase):
    def test_win_sizes(self):
        z = np.zeros((100, 100))
        w = win_sizes(z, [0.5, 0.38, 0.25])
        self.assertEqual(w, [50, 38, 25])
        z = np.zeros((100, 50))
        w = win_sizes(z, [0.5, 0.38, 0.25])
        self.assertEqual(w, [25])

    def test_win_positions(self):
        z = np.zeros((100, 100))
        w = [50]
        p = list(win_positions(z, w))
        self.assertEqual(p, [(50, 0, 0), (50, 0, 25), (50, 0, 50),
            (50, 25, 0), (50, 25, 25), (50, 25, 50),
            (50, 50, 0), (50, 50, 25), (50, 50, 50)])

    def test_sub_images(self):
        z = np.zeros((100, 100))
        i = list(sub_images(z, [(50, 10, 10)]))
        self.assertEqual(i[0].shape[0], 50)
        self.assertEqual(i[0].shape[1], 50)

if __name__ == '__main__':
    unittest.main()
