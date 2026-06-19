#%%


import cv2
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%


im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)


im_medianblur = cv2.medianBlur(
    im,
    5
)

plt.figure()
plt.imshow(im_medianblur)
plt.show()
#%%


#%%


im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)


im_meanblur = cv2.blur(
    im,
    (3, 3)
)

plt.figure()
plt.imshow(im_meanblur)
plt.show()
#%%


#%%


im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)


im_gaussianblur = cv2.GaussianBlur(
    im,
    (5, 5),
    0
)

plt.figure()
plt.imshow(im_gaussianblur)
plt.show()
#%%


#%%


im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)


sharpen_1 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])


im_sharpen1 = cv2.filter2D(
    im,
    -1,
    sharpen_1
)

plt.figure()
plt.imshow(im_sharpen1)


sharpen_2 = np.array([
    [0, -1, 0],
    [-1, 8, -1],
    [0, 1, 0]
]) / 4.0


im_sharpen2 = cv2.filter2D(
    im,
    -1,
    sharpen_2
)

plt.figure()
plt.imshow(im_sharpen2)
#%%
