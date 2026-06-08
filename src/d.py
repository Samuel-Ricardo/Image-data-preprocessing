#%%
# ═══════════════════════════════════════════════════════════
# SEÇÃO 1.4.5 - PROCESSAMENTO MORFOLÓGICO
# ═══════════════════════════════════════════════════════════

import cv2
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%
# ETAPA 1 - Ler e binarizar a imagem.

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
# ETAPA 2 - Definir elementos estruturantes.

# Define os elementos estruturantes.
element = cv2.getStructuringElement(
    cv2.MORPH_CROSS,
    (5, 5)
)

plt.imshow(element, 'gray')
#%%


#%%
# ETAPA 3 - Erosão.

# Realiza erosão da imagem.
eroded = cv2.erode(
    bin_img,
    element
)

# Exibe a imagem erodida.
plt.imshow(eroded, 'gray')

# Imagem original.
plt.figure()
plt.imshow(bin_img, 'gray')
#%%


#%%
# ETAPA 4 - Dilatação.

# Realiza dilatação da imagem.
dilated = cv2.dilate(
    bin_img,
    element
)

# Exibe a imagem dilatada.
plt.imshow(dilated, 'gray')

# Imagem original.
plt.figure()
plt.imshow(bin_img, 'gray')
#%%
