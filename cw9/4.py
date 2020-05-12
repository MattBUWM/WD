import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dt=pd.read_table('cw9/datasets/iris.data', header=None, delimiter=',')
dt.columns=['sepal lenght','sepal width','petal lenght','petal width','class']
fig, ax=plt.subplots()
for x,y in [['#ff0000','Iris-setosa'],['#00ff00','Iris-versicolor'],['#0000ff','Iris-virginica']]:
    dt[dt['class']==y].plot.scatter('petal lenght', 'petal width', c=x, label=y, ax=ax)
ax.legend()
plt.show()