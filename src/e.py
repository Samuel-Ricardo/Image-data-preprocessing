#%%
# ═══════════════════════════════════════════════════════════
# SEÇÃO 1.4.6 - FILTRAGEM DE IMAGENS
# ═══════════════════════════════════════════════════════════

import cv2
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%
# ETAPA 1 - Aplicar filtro mediana.

im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)

# Chama a API de filtro mediana
# do OpenCV.
im_medianblur = cv2.medianBlur(
    im,
    5
)

plt.figure()
plt.imshow(im_medianblur)
plt.show()
#%%


#%%
# ETAPA 2 - Aplicar filtro média.

im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)

# Chama a API de filtro média
# do OpenCV.
im_meanblur = cv2.blur(
    im,
    (3, 3)
)

plt.figure()
plt.imshow(im_meanblur)
plt.show()
#%%


#%%
# ETAPA 3 - Aplicar filtro Gaussiano.

im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)

# Chama a API de filtro Gaussiano
# do OpenCV.
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
# ETAPA 4 - Aplicar nitidez na imagem.

im = cv2.imread('data/panda.jpg')

im = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.imshow(im)

# Operador de nitidez.
sharpen_1 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])

# Usa filter2D para filtragem.
im_sharpen1 = cv2.filter2D(
    im,
    -1,
    sharpen_1
)

plt.figure()
plt.imshow(im_sharpen1)

# Operador de nitidez 2.
sharpen_2 = np.array([
    [0, -1, 0],
    [-1, 8, -1],
    [0, 1, 0]
]) / 4.0

# Usa filter2D para filtragem.
im_sharpen2 = cv2.filter2D(
    im,
    -1,
    sharpen_2
)

plt.figure()
plt.imshow(im_sharpen2)
#%%
