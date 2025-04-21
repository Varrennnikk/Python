import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris #Example for Assignment 1

# Задание 1: Диаграмма рассеяния (используем пример iris)
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

plt.figure(figsize=(8, 6))
for i in range(len(iris.target_names)):
    subset = df[df['target'] == i]
    plt.scatter(subset['petal length (cm)'], subset['petal width (cm)'],
                label=iris.target_names[i])

plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Iris Petal Sizes')
plt.legend()
plt.show()


# Задание 2: График временных рядов (пример с синтетическими данными)
dates = pd.date_range('1950-01-01', periods=100, freq='YS') #Year start
series1 = [x + (x*x*0.01) for x in range(20,120)]
series2 = [x + (x*x*0.002) for x in range(5, 105)]

df_ts = pd.DataFrame({'date': dates, 'series1': series1, 'series2':series2})


plt.figure(figsize=(10, 6))
plt.plot(df_ts['date'], df_ts['series1'], label='Series 1')
plt.plot(df_ts['date'], df_ts['series2'], label='Series 2')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Example')
plt.legend()
plt.grid(True)
plt.show()
