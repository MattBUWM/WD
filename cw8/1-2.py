import pandas as pd
import numpy as np
import xlrd
import openpyxl

def pp1(df):
    print(df[df['Liczba']>1000])

def pp2(df):
    print(df[df['Imie']=='MATEUSZ'])

def pp3(df):
    print("liczba urodzonych dieci:",df['Liczba'].sum())

def pp4(df):
    print("Liczba urodzonych dzieci w latach 2000-2005:",df['Liczba'].where(df['Rok']<=2005,0).sum())

def pp5(df):
    print("Liczba urodzonych dziewczynek:",df['Liczba'].where(df['Plec']=="K",0).sum())
    print("Liczba urodzonych chłopców:",df['Liczba'].where(df['Plec']=="M",0).sum())

def pp6(df):
    dfr=df.sort_values(['Liczba'],ascending=False).groupby(['Rok','Plec'])
    print(dfr.head(1).sort_values(['Rok','Plec']))

def pp7(df):
    dfp=df[df['Plec']=='K'].groupby(['Imie'])['Liczba'].sum()
    print(dfp.sort_values(ascending=False).head(1))
    dfp=df[df['Plec']=='M'].groupby(['Imie'])['Liczba'].sum()
    print(dfp.sort_values(ascending=False).head(1))

df=pd.read_excel(pd.ExcelFile('cw8/datasets/imiona.xlsx'))

#pp1(df)
#pp2(df)
#pp3(df)
#pp4(df)
#pp5(df)
#pp6(df)
#pp7(df)