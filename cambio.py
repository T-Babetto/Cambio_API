import requests 

URL = 'https://api.hgbrasil.com/finance'

resposta = requests.get(f'{URL}')

dados = resposta.json()['results']['currencies']

dolar = dados['USD']['buy'] 
euro = dados['EUR']['buy']

real = float(input('Digite um valor em real:'))
converter_dolar = real/dolar
converter_euro = real/euro


print(f'O valor digitado em Dólares(USD) é: {converter_dolar:.2f}')
print(f'O valor digitado em Euros(EUR) é: {converter_euro:.2f}')