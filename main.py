import pyautogui as pag
import pandas as pd
import time


pag.PAUSE = 0.5
#abrir navegador
pag.press('win')
pag.write('firefox')
pag.press('enter')

#escrever o link no browser
pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pag.press('enter')
time.sleep(4)

#selecionar os campos na tela
#pag.press('tab')
pag.click(x=475, y=401)
pag.write('teste.gabriel@gmail.com')
pag.press('tab')
pag.write('sua senha aqui')
pag.press('tab')
pag.press('enter')

#espera para aguardar o site
time.sleep(4)

tabela = pd.read_csv('produtos.csv')
#print(tabela)

#preencher o formulário 
for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])
    marca = str(tabela.loc[linha, 'marca'])
    tipo = str(tabela.loc[linha, 'tipo'])
    categoria = str(tabela.loc[linha, 'categoria'])
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    custo = str(tabela.loc[linha, 'custo'])
    obs = str(tabela.loc[linha, 'obs'])

    pag.click(x=573, y=278)
    pag.write(codigo)
    pag.press('tab')
    pag.write(marca)
    pag.press('tab')
    pag.write(tipo)
    pag.press('tab')
    pag.write(categoria)
    pag.press('tab')
    pag.write(preco_unitario)
    pag.press('tab')
    pag.write(custo)
    pag.press('tab')
    pag.write(obs)
    pag.press('tab')
    pag.press('enter')
    pag.scroll(5000)