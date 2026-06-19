#%%


import numpy as np
import cv2
from matplotlib import pyplot as plt

%matplotlib inline
#%%


#%%


def linear_trans(img, k, b=0):

    trans_list = [
        (np.float32(x) * k + b)
        for x in range(256)
    ]
    trans_table = np.array(trans_list)


    trans_table[trans_table > 255] = 255
    trans_table[trans_table < 0] = 0
    trans_table = np.round(
        trans_table
    ).astype(np.uint8)


    return cv2.LUT(img, trans_table)
#%%


#%%
im = cv2.imread(r'data/panda.jpg', 0)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im, 'gray')


im_inversion = linear_trans(
    im,
    -1,
    255
)

plt.subplot(2, 2, 2)
plt.title('reversed')
plt.imshow(im_inversion, 'gray')


im_stretch = linear_trans(im, 1.2)

plt.subplot(2, 2, 3)
plt.title('stretch')
plt.imshow(im_stretch, 'gray')


im_compress = linear_trans(im, 0.4)

plt.subplot(2, 2, 4)
plt.title('compress')
plt.imshow(im_compress, 'gray')
#%%


#%%


def gamma_trans(img, gamma):


    gamma_list = [
        np.power(x / 255.0, gamma) * 255.0
        for x in range(256)
    ]


    gamma_table = np.round(
        np.array(gamma_list)
    ).astype(np.uint8)


    return cv2.LUT(img, gamma_table)
#%%


#%%
im = cv2.imread(r'data/panda.jpg', 0)

plt.figure(figsize=(8, 8))
plt.subplot(1, 3, 1)
plt.title('original')
plt.imshow(im, 'gray')


im_gamma05 = gamma_trans(im, 0.5)

plt.subplot(1, 3, 2)
plt.title('gamma=0.5')
plt.imshow(im_gamma05, 'gray')


im_gamma2 = gamma_trans(im, 2)

plt.subplot(1, 3, 3)
plt.title('gamma=2')
plt.imshow(im_gamma2, 'gray')
#%%


#%%


import cv2
from matplotlib import pyplot as plt

im = cv2.imread(r'data/panda.jpg', 0)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.imshow(im, 'gray')


im_equa1 = cv2.equalizeHist(im)

plt.subplot(2, 2, 3)
plt.imshow(im_equa1, 'gray')


plt.subplot(2, 2, 2)
plt.hist(
    im.ravel(),
    256,
    [0, 256],
    label='org'
)
plt.legend()


plt.subplot(2, 2, 4)
plt.hist(
    im_equa1.ravel(),
    256,
    [0, 256],
    label='equalize'
)
plt.legend()
plt.show()
#%%


#%%


img = cv2.imread(
    r'data/panda.jpg',
    0
)


ret1, th1 = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY
)


ret2, th2 = cv2.threshold(
    img,
    0,
    255,
    cv2.THRESH_OTSU
)

print(
    'Simple threshold value:',
    ret1
)
print(
    'Optimal threshold value:',
    ret2
)

plt.figure(figsize=(8, 8))
plt.subplot(221)
plt.imshow(img, 'gray')

plt.subplot(222)


plt.hist(img.ravel(), 256)

plt.subplot(223)
plt.imshow(th1, 'gray')

plt.subplot(224)
plt.imshow(th2, 'gray')
#%%
