#%%


import cv2
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%


img = cv2.imread(
    'data/panda.jpg',
    0
)

_, bin_img = cv2.threshold(
    img,
    0,
    255,
    cv2.THRESH_OTSU
)

plt.imshow(bin_img, 'gray')
#%%


#%%


element = cv2.getStructuringElement(
    cv2.MORPH_CROSS,
    (5, 5)
)

plt.imshow(element, 'gray')
#%%


#%%


eroded = cv2.erode(
    bin_img,
    element
)


plt.imshow(eroded, 'gray')


plt.figure()
plt.imshow(bin_img, 'gray')
#%%


#%%


dilated = cv2.dilate(
    bin_img,
    element
)


plt.imshow(dilated, 'gray')


plt.figure()
plt.imshow(bin_img, 'gray')
#%%
