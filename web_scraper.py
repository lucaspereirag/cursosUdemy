from bs4 import BeautifulSoup
import requests


#Pega toda o conteúdo e jogará para a variável site.
site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())

