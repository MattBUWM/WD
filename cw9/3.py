import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df=pd.read_excel(pd.ExcelFile('cw9/datasets/imiona.xlsx'))
maxRok=df.copy().agg({'Rok':['max']})
df[df['Rok'] > maxRok.values[0,0]-5].groupby(['Plec']).agg({'Liczba':['sum']}).plot.pie(subplots=True, autopct='%.2f %%', figsize=(6, 6))
plt.show()