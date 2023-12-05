import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.mercadolivre.com.br/estatistica-basica-probabilidade-e-inferncia-de-morettin-luiz-gonzaga-editora-pearson-capa-mole-edico-1-em-portugus-2009/p/MLB24978763?pdp_filters=category:MLB1196%7Cshipping_cost:free#searchVariation=MLB24978763&position=1&search_layout=grid&type=product&tracking_id=290c0ee5-5b5c-4031-99f8-9f4d7f57c0b8'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#titulo = soup.find('h1', class_='ui-pdp-title').text
titulo = soup.xpath('.ui-pdp-collapsable__container')

print(titulo)

