from bs4 import BeautifulSoup
import urllib3
import pandas as pd

def get_games_info_from_page(url):
    gry={
        'tytul':[],
        'platforma':[],
        'data wydania':[],
        'ocena':[]
    }
    soup=BeautifulSoup(http.request('GET',url).data,'lxml')
    for x in soup.find_all('table'):
        for y in x.find_all('td',{'class':'clamp-summary-wrap'}):
            gry['tytul'].append(y.find('h3').string.strip())
            for z in y.find_all('div'):
                if z['class'] == ['clamp-score-wrap']:
                    gry['ocena'].append(int(z.find('div').string.strip()))
                elif z['class'] == ['clamp-details']:
                    gry['platforma'].append(z.find('span',{'class':'data'}).string.strip())
                    gry['data wydania'].append(z.find('span',{'class':None}).string)
    return gry

url='https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page='
http=urllib3.PoolManager()
#zadanie3
gry=get_games_info_from_page(url+'0')
df=pd.DataFrame(gry)
#zadanie4
for x in range(1,10):
    gry=get_games_info_from_page(url+str(x))
    df=df.append(pd.DataFrame(gry),ignore_index=True)
print(df.where(df['platforma']=='PC').sort_values('ocena',ascending=False).head(10))
