#%%

respostas = [
    ("1", "No limiar manual o valor e fixo pelo usuario; no Otsu o limiar e calculado automaticamente pelo histograma da imagem."),
    ("2", "Sim. Otsu escolhe o limiar que minimiza a variancia intra-classe, produzindo segmentacao melhor quando o histograma e bimodal."),
]

print("Questoes Lab 06 - Limiarizacao")
print("=" * 45)
for numero, resposta in respostas:
    print(f"{numero}. {resposta}\n")


#%%


#%%


#%%


#%%


#%%


#%%


#%%


import cv2
import numpy as np

IMG = 'data/panda.jpg'

import os
if os.path.isfile(IMG):
    img = cv2.imread(IMG, 0)


    ret_manual, th_manual = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


    ret_otsu, th_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

    print("=" * 50)
    print("COMPARAÇÃO: Manual vs Otsu")
    print("=" * 50)
    print(f"\nLimiar Manual: {ret_manual}")
    print(f"Limiar Otsu:   {ret_otsu}")
    print(f"\nPixels brancos (manual): {np.sum(th_manual == 255)}")
    print(f"Pixels brancos (Otsu):   {np.sum(th_otsu == 255)}")
    print(f"\nO Otsu escolheu {ret_otsu:.0f} como limiar ótimo,")
    print(f"que é {'menor' if ret_otsu < 127 else 'maior'} que o manual (127).")
    print(f"Isso indica que a distribuição da imagem tem mais pixels")
    print(f"{'escuros' if ret_otsu < 127 else 'claros'} do que o ponto médio sugere.")
else:
    print("Imagem não encontrada. Execute a partir de 06/src/")
    print("Resultados esperados:")
    print("  Limiar Manual: 127.0")
    print("  Limiar Otsu:   108.0")
#%%
