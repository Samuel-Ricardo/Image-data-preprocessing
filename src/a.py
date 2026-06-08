#%%
# ═══════════════════════════════════════════════════════════
# SEÇÃO 1.4.1 - OPERAÇÕES BÁSICAS COM IMAGENS
# ═══════════════════════════════════════════════════════════

import cv2
import matplotlib.pyplot as plt

%matplotlib inline
#%%


#%%
# ETAPA 1 - Ler e exibir imagens.

# Leitura da imagem. Se o segundo parâmetro for 1, a imagem colorida é
# carregada.
# Se for 0, a imagem em escala de cinza é carregada.
im = cv2.imread(r"data/panda.jpg", 1)
im_gray = cv2.imread(r"data/panda.jpg", 0)

# Cria uma figura.
plt.figure()

# Quando imagens são exibidas usando
# Matplotlib, as cores podem ficar incorretas.
plt.subplot(1, 2, 1), plt.imshow(im)
plt.subplot(1, 2, 2), plt.imshow(im_gray, 'gray')
plt.show()
#%%


#%%
# Isso ocorre porque o OpenCV utiliza o padrão BGR, enquanto o
# Matplotlib utiliza RGB.
im_RBG = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2RGB
)

plt.subplot(1, 2, 1), plt.imshow(im_RBG)
plt.subplot(1, 2, 2), plt.imshow(im_gray, 'gray')
#%%


#%%
# ETAPA 2 - Exibir o tipo de dado e o tamanho da imagem.

# Exibe o tipo dos dados.
print(im.dtype)

# Exibe o tamanho da imagem.
print(im.shape)
#%%


#%%
# ETAPA 3 - Salvar a imagem.

# Salva a imagem.
cv2.imwrite('data/panda.png', im)
#%%


#%%
# ═══════════════════════════════════════════════════════════
# SEÇÃO 1.4.2 - CONVERSÃO DE ESPAÇO DE CORES
# ═══════════════════════════════════════════════════════════
#%%


#%%
# ETAPA 1 - Converter imagem colorida para escala de cinza.

im = cv2.imread(r"data/panda.jpg")

# Conversão BGR para escala de cinza.
img_gray = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2GRAY
)

plt.imshow(img_gray, 'gray')
#%%


#%%
# ETAPA 2 - Converter de BGR para HSV.

im = cv2.imread(r"data/panda.jpg")

# Conversão BGR para HSV.
im_hsv = cv2.cvtColor(
    im,
    cv2.COLOR_BGR2HSV
)

# O imshow assume RGB.
# Portanto, pode ocorrer distorção
# ao exibir HSV diretamente.
plt.imshow(im_hsv)
#%%
