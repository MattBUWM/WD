import pandas as pd
import numpy as np

def pp1(df):
    print(df['Sprzedawca'].unique())

def pp2(df):
    print(df.sort_values('Utarg',ascending=False)['Utarg'].head(5))

def pp3(df):
    print(df.groupby('Sprzedawca')['idZamowienia'].count())

def pp4(df):
    print(df.groupby('Kraj')['idZamowienia'].count())

def pp5(df):
    dfc=df.copy()
    dfc['Data zamowienia']=pd.to_datetime(dfc['Data zamowienia'])
    print(dfc[(dfc['Kraj']=='Polska') & (dfc['Data zamowienia'].dt.year==2005)]['idZamowienia'].count())

def pp6(df):
    dfc=df.copy()
    dfc['Data zamowienia']=pd.to_datetime(dfc['Data zamowienia'])
    print(dfc[dfc['Data zamowienia'].dt.year==2004]['Utarg'].mean())

def pp7(df):
    dfc=df.copy()
    dfc['Data zamowienia']=pd.to_datetime(dfc['Data zamowienia'])
    dfc[dfc['Data zamowienia'].dt.year==2004].to_csv('cw8/zamowienia_2004.csv',sep=';',index=False)
    dfc[dfc['Data zamowienia'].dt.year==2005].to_csv('cw8/zamowienia_2005.csv',sep=';',index=False)

df=pd.read_csv('cw8/datasets/zamowienia.csv',delimiter=';')

#pp1(df)
#pp2(df)
#pp3(df)
#pp4(df)
#pp5(df)
#pp6(df)
pp7(df)