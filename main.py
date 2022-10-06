import config
import requests
from datetime import datetime
from models.cotacao import Cotacao

URL_BASE = 'https://hgbrasil.com/finance'.format('?key={0}', config.api_key)

def consultar_dados_financeiros() -> Cotacao:
    requisicao = requests.get(URL_BASE)
    dados = requisicao.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now)
    return Cotacao(dolar = dolar, euro = euro, data_hora = data_hora)


if __name__ == '__main__':
    print(URL_BASE)
    print(config.api_key)

