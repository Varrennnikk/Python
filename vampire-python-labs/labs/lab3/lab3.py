import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# Задание 1: Диаграмма рассеяния

# Загрузка данных (пример с использованием iris dataset)
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

# Выбор факторов и классов
x_factor = 'sepal length (cm)'
y_factor = 'sepal width (cm)'
class_column = 'target'

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_factor, y=y_factor, hue=class_column, data=iris_df, palette='viridis')
plt.xlabel(x_factor)
plt.ylabel(y_factor)
plt.title('Диаграмма рассеяния для Iris Dataset')
plt.legend()
plt.grid(True)
plt.show()


# Задание 2: График временных рядов (пример с синтетическими данными)

# Создание данных временных рядов
dates = pd.date_range('2023-01-01', periods=100, freq='D')
series1 = [i*1.1 + 5*(-1)**i for i in range(100)]
series2 = [i*0.9 + 3*(-1)**i for i in range(100)]

time_series_df = pd.DataFrame({'Date': dates, 'Series1': series1, 'Series2': series2})
time_series_df.set_index('Date', inplace=True)

# Построение графика временных рядов
plt.figure(figsize=(10, 6))
plt.plot(time_series_df.index, time_series_df['Series1'], label='Series 1')
plt.plot(time_series_df.index, time_series_df['Series2'], label='Series 2')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.title('График временных рядов')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Чтобы метки не перекрывались
plt.show()
