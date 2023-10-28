# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import re

import requests
from bs4 import BeautifulSoup

url = 'https://nerdfilmes.com.br/guardioes-da-galaxia-vol-3-torrent-2023-dublado-download/'
response = requests.get(url)
# raw_html = response.text
# parsed_html = BeautifulSoup(raw_html, 'html.parser')
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

guardians_heading = parsed_html.select_one('body > div.elementor.elementor-1115.elementor-location-single.post-5667.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-dublado.category-filmes > div > div > div.elementor-element.elementor-element-717a578.e-con-full.e-flex.e-con > div.elementor-element.elementor-element-92e492d.elementor-widget.elementor-widget-theme-post-title.elementor-page-title.elementor-widget-heading > div > h1')
print(guardians_heading)
print()

if guardians_heading is not None:
    print(guardians_heading.text)

print()

guardians_sinopse = parsed_html.select_one('body > div.elementor.elementor-1115.elementor-location-single.post-5667.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-dublado.category-filmes > div > div > div.elementor-element.elementor-element-717a578.e-con-full.e-flex.e-con > div.elementor-element.elementor-element-dff4791.elementor-widget.elementor-widget-theme-post-content > div > p:nth-child(5)')
print(guardians_sinopse)
print()

if guardians_sinopse is not None:
    print(guardians_sinopse.text)