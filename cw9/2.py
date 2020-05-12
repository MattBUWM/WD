import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df=pd.read_excel(pd.ExcelFile('cw9/datasets/imiona.xlsx'))
df.groupby(['Plec'])['Liczba'].sum().plot.bar()
plt.show()