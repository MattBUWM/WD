import requests
from lxml import html

url = "https://boardgamegeek.com"
data = requests.get(url)
page = html.fromstring(data.text)

#chodźby nie wiem co próbuję nie chce działać jak powinno, nawet jak bezpośrednio z przeglądarki skopiuję xpath dla elementów <a>
for x in range (2,6+2+1):
    xpath='//*[@id="results_1"]/div/div/div[2]/div['+str(x)+']/h2/a'
    foundElement = page.xpath(xpath)
    print(foundElement)
    print(foundElement[0].get('ng-href'))