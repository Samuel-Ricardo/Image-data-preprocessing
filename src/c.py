#%%
# ═══════════════════════════════════════════════════════════
# SEÇÃO 1.4.4 - TRANSFORMAÇÕES EM ESCALA DE CINZA
# ═══════════════════════════════════════════════════════════

import numpy as np
import cv2
from matplotlib import pyplot as plt

%matplotlib inline
#%%


#%%
# ETAPA 1 - Inversão, alongamento em tons de cinza, compressão em tons de cinza.

# Define a função de transformação linear.
# Para k > 1:
# alongamento da escala de cinza.
#
# Para 0 < k < 1:
# compressão da escala de cinza.
#
# Para k = -1 e b = 255:
# inversão da imagem.
def linear_trans(img, k, b=0):
    # Cria a tabela de transformação.
    trans_list = [
        (np.float32(x) * k + b)
        for x in range(256)
    ]
    trans_table = np.array(trans_list)

    # Limita os valores entre 0 e 255.
    trans_table[trans_table > 255] = 255
    trans_table[trans_table < 0] = 0
    trans_table = np.round(
        trans_table
    ).astype(np.uint8)

    # Aplica a transformação.
    return cv2.LUT(img, trans_table)
#%%


#%%
im = cv2.imread(r'data/panda.jpg', 0)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(im, 'gray')

# Inversão.
im_inversion = linear_trans(
    im,
    -1,
    255
)

plt.subplot(2, 2, 2)
plt.title('reversed')
plt.imshow(im_inversion, 'gray')

# Alongamento.
im_stretch = linear_trans(im, 1.2)

plt.subplot(2, 2, 3)
plt.title('stretch')
plt.imshow(im_stretch, 'gray')

# Compressão.
im_compress = linear_trans(im, 0.4)

plt.subplot(2, 2, 4)
plt.title('compress')
plt.imshow(im_compress, 'gray')
#%%


#%%
# ETAPA 2 - Transformação Gamma.

def gamma_trans(img, gamma):
    # Normaliza para 1, realiza o cálculo gamma
    # e depois restaura para [0,255].
    gamma_list = [
        np.power(x / 255.0, gamma) * 255.0
        for x in range(256)
    ]

    # Converte a lista para np.array
    # e define o tipo de dado como uint8.
    gamma_table = np.round(
        np.array(gamma_list)
    ).astype(np.uint8)

    # Usa a tabela de consulta do OpenCV
    # para modificar os valores em escala de cinza.
    return cv2.LUT(img, gamma_table)
#%%


#%%
im = cv2.imread(r'data/panda.jpg', 0)

plt.figure(figsize=(8, 8))
plt.subplot(1, 3, 1)
plt.title('original')
plt.imshow(im, 'gray')

# Utiliza gamma = 0.5 para realçar
# regiões escuras e comprimir regiões claras.
im_gamma05 = gamma_trans(im, 0.5)

plt.subplot(1, 3, 2)
plt.title('gamma=0.5')
plt.imshow(im_gamma05, 'gray')

# Utiliza gamma = 2 para realçar
# regiões claras e comprimir regiões escuras.
im_gamma2 = gamma_trans(im, 2)

plt.subplot(1, 3, 3)
plt.title('gamma=2')
plt.imshow(im_gamma2, 'gray')
#%%


#%%
# ETAPA 3 - Equalização de histograma.

import cv2
from matplotlib import pyplot as plt

im = cv2.imread(r'data/panda.jpg', 0)

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.imshow(im, 'gray')

# Chama a API de equalização
# de histograma do OpenCV.
im_equa1 = cv2.equalizeHist(im)

plt.subplot(2, 2, 3)
plt.imshow(im_equa1, 'gray')

# Exibe o histograma da imagem original.
plt.subplot(2, 2, 2)
plt.hist(
    im.ravel(),
    256,
    [0, 256],
    label='org'
)
plt.legend()

# Exibe o histograma da imagem equalizada.
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
# ETAPA 4 - Aplicar binarização na imagem.

img = cv2.imread(
    r'data/panda.jpg',
    0
)

# Segmentação simples por limiar.
ret1, th1 = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY
)

# Método de Otsu.
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
# O método ravel converte
# a matriz em vetor unidimensional.
plt.hist(img.ravel(), 256)

plt.subplot(223)
plt.imshow(th1, 'gray')

plt.subplot(224)
plt.imshow(th2, 'gray')
#%%
