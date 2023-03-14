# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:35:21 2023

Código para analisar a variância e desvio padrão da expectativa de vida do brasileiro

@author: Gabriel Ratão
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
#%% imporando a base de dados
tabela = pd.read_excel(r"C:\Users\User\Documents\Python\bases_dados\expectativa_vida_Brasil\esperanca_de_vida_2000a2014.xlsx", "Tabela")
display(tabela)

#%% gerando os valores de variância, média e desvio padrão


media = sum(tabela['idade']) / len(tabela['idade'])
print(f'media {media}')

inter = 0
for i in tabela['idade']:
    inter = inter + (i - media)**2
var = inter / len(tabela['idade'])
desvioP = var**(1/2)

print(f'Variancia: {var}\nDesvio Padrao: {desvioP}')



#%%


plt.figure(figsize=(10, 5))



plt.scatter(tabela["ano"], tabela["idade"])
plt.xlabel('ano (2000-2014)')
plt.ylabel('expectativa de vida')
plt.suptitle('Expectativa de vida no Brasil')

plt.annotate(f'Média: {media}\nDesvião Padrão: {desvioP:.2f}\nVariância: {var:.2f}', xy=(2000, 74), xytext=(2000, 74), 
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


plt.show()
#%%