#%%


import cv2
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%


im = cv2.imread(r"data/panda.jpg", 1)
im_gray = cv2.imread(r"data/panda.jpg", 0)


plt.figure()


plt.subplot(1, 2, 1), plt.imshow(im)
plt.subplot(1, 2, 2), plt.imshow(im_gray, 'gray')
plt.show()
#%%


#%%


im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.subplot(1, 2, 1), plt.imshow(im_RBG)
plt.subplot(1, 2, 2), plt.imshow(im_gray, 'gray')
#%%


#%%


print(im.dtype)


print(im.shape)
#%%


#%%


cv2.imwrite('data/panda.png', im)
#%%


#%%


#%%


#%%


im = cv2.imread(r"data/panda.jpg")


img_gray = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2GRAY
)

plt.imshow(img_gray, 'gray')
#%%


#%%


im = cv2.imread(r"data/panda.jpg")


im_hsv = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2HSV
)


plt.imshow(im_hsv)
#%%
