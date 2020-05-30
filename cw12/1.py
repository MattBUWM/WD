import requests
from lxml import html

url = "https://boardgamegeek.com"
data = requests.get(url)
page = html.fromstring(data.text)
xpath='//*[@id="results_1"]//a'
foundElements = page.xpath(xpath)
for element in foundElements :
    print(element.text)
