#Data plotting using panda
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('TrData.csv')

print(df.head())

df['DOCNUMBER'].plot()

plt.show()