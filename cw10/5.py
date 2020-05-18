import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dt=pd.read_table('cw10/datasets/iris.data', header=None, delimiter=',')
dt.columns=['sepal lenght','sepal width','petal lenght','petal width','class']
dt['abs']=np.abs(dt['sepal lenght']-dt['sepal width'])
dt['c']=np.random.randint(0, 50, dt.shape[0])
plt.scatter('sepal lenght','sepal width',c='c',s='abs',data=dt)
plt.show()