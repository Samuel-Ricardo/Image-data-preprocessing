#%%
# ═══════════════════════════════════════════════════════════
# SEÇÃO 1.4.3 - TRANSFORMAÇÕES GEOMÉTRICAS
# ═══════════════════════════════════════════════════════════

import numpy as np
import cv2
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%
# ETAPA 1 - Aplicar translação na imagem.

# Define a função de translação.
def translate(img, x, y):
    # Obtém o tamanho da imagem.
    (h, w) = img.shape[:2]

    # Define a matriz de translação.
    M = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])

    # Executa a transformação afim.
    shifted = cv2.warpAffine(
        img,
        M,
        (w, h)
    )

    return shifted
#%%


#%%
# Carrega a imagem.
im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)

# Move 500 pixels para baixo.
shifted_1 = translate(im_RBG, 0, 500)

plt.subplot(2, 2, 2)
plt.title('down move 500 pixels')
plt.imshow(shifted_1)

# Move 1000 pixels para esquerda.
shifted_2 = translate(im_RBG, -1000, 0)

plt.subplot(2, 2, 3)
plt.title('left move 1000 pixels')
plt.imshow(shifted_2)

# Move 500 pixels para direita
# e 1000 pixels para baixo.
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
# ETAPA 2 - Aplicar rotação na imagem.

# Define a função de rotação.
def rotate(
    img,
    angle,
    center=None,
    scale=1.0
):
    # Obtém o tamanho da imagem.
    (h, w) = img.shape[:2]

    # Caso o centro não seja informado,
    # utiliza o centro da imagem.
    if center is None:
        center = (w / 2, h / 2)

    # Calcula a matriz de rotação.
    M = cv2.getRotationMatrix2D(
        center,
        angle,
        scale
    )

    # Executa a transformação afim.
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

# Rotação de 45 graus anti-horário.
rotated_45 = rotate(im_RBG, 45)

plt.subplot(2, 2, 2)
plt.title(
    'rotate 45 degree counter-clockwise'
)
plt.imshow(rotated_45)

# Rotação de 20 graus horário.
rotated_minus20 = rotate(im_RBG, -20)

plt.subplot(2, 2, 3)
plt.title(
    'rotate 45 degree clockwise'
)
plt.imshow(rotated_minus20)

# Rotação de 90 graus anti-horário.
rotated_90 = rotate(im_RBG, 90)

plt.subplot(2, 2, 4)
plt.title(
    'rotate 90 degree counter-clockwise'
)
plt.imshow(rotated_90)
#%%


#%%
# ETAPA 3 - Aplicar espelhamento na imagem.

im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)

# Espelhamento horizontal.
im_flip0 = cv2.flip(im_RBG, 0)

plt.subplot(2, 2, 2)
plt.title('Mirror Horizontally')
plt.imshow(im_flip0)

# Espelhamento vertical.
im_flip1 = cv2.flip(im_RBG, 1)

plt.subplot(2, 2, 3)
plt.title('Mirror Vertically')
plt.imshow(im_flip1)
#%%


#%%
# ETAPA 4 - Redimensionar a imagem.

im = cv2.imread('data/panda.jpg')

im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im_RBG)

# Obtém o tamanho da imagem.
(h, w) = im_RBG.shape[:2]

# Define o novo tamanho.
dst_size = (2000, 3000)

# Interpolação vizinho mais próximo.
method = cv2.INTER_NEAREST

# Redimensionamento.
resized = cv2.resize(
    im_RBG,
    dst_size,
    interpolation=method
)

plt.subplot(2, 2, 2)
plt.title('INTER_NEAREST')
plt.imshow(resized)

# Define novo tamanho.
dst_size = (5000, 5000)

# Interpolação bilinear.
method = cv2.INTER_LINEAR

# Redimensionamento.
resized_linear = cv2.resize(
    im_RBG,
    dst_size,
    interpolation=method
)

plt.subplot(2, 2, 3)
plt.title('INTER_LINEAR')
plt.imshow(resized_linear)
#%%
