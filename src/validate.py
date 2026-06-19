"""Validation script - tests all Lab 6 operations without GUI display."""
import cv2
import numpy as np

IMG = 'data/panda.jpg'


im = cv2.imread(IMG, 1)
im_gray = cv2.imread(IMG, 0)
im_RGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
assert im.dtype == np.uint8
assert im.shape == (2600, 3914, 3)
print("[OK] a.py - Basic ops + Color space")


(h, w) = im.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 200]])
shifted = cv2.warpAffine(im, M, (w, h))
assert shifted.shape == im.shape

center = (w / 2, h / 2)
M_rot = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(im, M_rot, (w, h))
assert rotated.shape == im.shape

flipped = cv2.flip(im_RGB, 0)
assert flipped.shape == im_RGB.shape

resized = cv2.resize(im_RGB, (2000, 3000), interpolation=cv2.INTER_NEAREST)
assert resized.shape == (3000, 2000, 3)
print("[OK] b.py - Geometric transforms")


def linear_trans(img, k, b=0):
    trans_list = [(np.float32(x) * k + b) for x in range(256)]
    trans_table = np.array(trans_list)
    trans_table[trans_table > 255] = 255
    trans_table[trans_table < 0] = 0
    trans_table = np.round(trans_table).astype(np.uint8)
    return cv2.LUT(img, trans_table)

def gamma_trans(img, gamma):
    gamma_list = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_list)).astype(np.uint8)
    return cv2.LUT(img, gamma_table)

im_inv = linear_trans(im_gray, -1, 255)
im_stretch = linear_trans(im_gray, 1.2)
im_compress = linear_trans(im_gray, 0.4)
im_g05 = gamma_trans(im_gray, 0.5)
im_g2 = gamma_trans(im_gray, 2)
im_eq = cv2.equalizeHist(im_gray)
ret1, th1 = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(im_gray, 0, 255, cv2.THRESH_OTSU)
assert ret1 == 127.0
assert ret2 > 0
print("[OK] c.py - Grayscale transforms (Otsu threshold:", ret2, ")")


_, bin_img = cv2.threshold(im_gray, 0, 255, cv2.THRESH_OTSU)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
eroded = cv2.erode(bin_img, element)
dilated = cv2.dilate(bin_img, element)
assert eroded.shape == bin_img.shape
assert dilated.shape == bin_img.shape
print("[OK] d.py - Morphological processing")


im_median = cv2.medianBlur(im, 5)
im_mean = cv2.blur(im, (3, 3))
im_gauss = cv2.GaussianBlur(im, (5, 5), 0)
sharpen_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
im_sharp = cv2.filter2D(im, -1, sharpen_1)
assert im_median.shape == im.shape
assert im_mean.shape == im.shape
assert im_gauss.shape == im.shape
assert im_sharp.shape == im.shape
print("[OK] e.py - Image filtering")

print("\n=== ALL VALIDATIONS PASSED ===")
