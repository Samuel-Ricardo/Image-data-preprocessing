#%%


import numpy as np
import cv2
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%


def translate(img, x, y):

    (h, w) = img.shape[:2]


    M = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])


    shifted = cv2.warpAffine(
        img,
        M,
        (w, h)
    )

    return shifted
#%%


#%%

im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)


shifted_1 = translate(im_RBG, 0, 500)

plt.subplot(2, 2, 2)
plt.title('down move 500 pixels')
plt.imshow(shifted_1)


shifted_2 = translate(im_RBG, -1000, 0)

plt.subplot(2, 2, 3)
plt.title('left move 1000 pixels')
plt.imshow(shifted_2)


shifted_3 = translate(
    im_RBG,
    500,
    1000
)

plt.subplot(2, 2, 4)
plt.title(
    'right move 500,down move 1000 pixels'
)
plt.imshow(shifted_3)
#%%


#%%


def rotate(
    img,
    angle,
    center=None,
    scale=1.0
):

    (h, w) = img.shape[:2]


    if center is None:
        center = (w / 2, h / 2)


    M = cv2.getRotationMatrix2D(
        center,
        angle,
        scale
    )


    rotated = cv2.warpAffine(
        img,
        M,
        (w, h)
    )

    return rotated
#%%


#%%
im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)


rotated_45 = rotate(im_RBG, 45)

plt.subplot(2, 2, 2)
plt.title(
    'rotate 45 degree counter-clockwise'
)
plt.imshow(rotated_45)


rotated_minus20 = rotate(im_RBG, -20)

plt.subplot(2, 2, 3)
plt.title(
    'rotate 45 degree clockwise'
)
plt.imshow(rotated_minus20)


rotated_90 = rotate(im_RBG, 90)

plt.subplot(2, 2, 4)
plt.title(
    'rotate 90 degree counter-clockwise'
)
plt.imshow(rotated_90)
#%%


#%%


im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)


im_flip0 = cv2.flip(im_RBG, 0)

plt.subplot(2, 2, 2)
plt.title('Mirror Horizontally')
plt.imshow(im_flip0)


im_flip1 = cv2.flip(im_RBG, 1)

plt.subplot(2, 2, 3)
plt.title('Mirror Vertically')
plt.imshow(im_flip1)
#%%


#%%


im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)


(h, w) = im_RBG.shape[:2]


dst_size = (2000, 3000)


method = cv2.INTER_NEAREST


resized = cv2.resize(
    im_RBG,
    dst_size,
    interpolation=method
)

plt.subplot(2, 2, 2)
plt.title('INTER_NEAREST')
plt.imshow(resized)


dst_size = (5000, 5000)


method = cv2.INTER_LINEAR


resized_linear = cv2.resize(
    im_RBG,
    dst_size,
    interpolation=method
)

plt.subplot(2, 2, 3)
plt.title('INTER_LINEAR')
plt.imshow(resized_linear)
#%%
