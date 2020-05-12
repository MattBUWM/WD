import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('cw8/datasets/zamowienia.csv',delimiter=';')
df.groupby('Sprzedawca')['idZamowienia'].count().plot.bar()
plt.show()