import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Comment this if the data visualisations doesn't work on your side
%matplotlib inline

plt.style.use('bmh')

df = pd.read_csv('C:\Users\suuser\Downloads\nyc-rolling-sales.csv')
df.head()
