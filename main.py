import requests
import json
import sqlite3
import datetime

requisicao = requests.get('https://api.hgbrasil.com/finance?key=2ebfe9dd')
valor = json.loads(requisicao.text)
'''print(valor) '''
dolar = valor['results']['currencies']['USD']['buy']
euro = valor['results']['currencies']['EUR']['buy']
real = float(input('Informe um valor (R$): '))
conversaodolar = real/dolar
conversaoeuro = real/euro
datahora = datetime.datetime.now()
print(f'Valor em dolar: {conversaodolar}')
print(f'Valor em euro: {conversaoeuro}')
print(f'Data e hora: {datahora}')

conexao = sqlite3.connect('cotacoes.db')
cursor = conexao.cursor()
# cursor.execute("CREATE TABLE cotacao (dolar real, euro real, datahora text)") 
cursor.execute("INSERT INTO cotacao (dolar, euro, datahora) VALUES (?,?,?);", (dolar,euro,datahora))
conexao.commit()
cursor.execute("SELECT * FROM Cotacao")
print(cursor.fetchall())
