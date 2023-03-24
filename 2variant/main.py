import pandas as pd

# Загрузка данных из Excel-файла
df = pd.read_excel('1.xlsx')
df = df.drop(index=60)
# Выбор всех столбцов, кроме столбца с датами
data = df.iloc[:, 1:]
# Вычисление среднего и стандартного отклонения для каждого вагона
means = data.mean(axis=0)
stds = data.std(axis=0)
# Выбор вагона с наибольшей температурой
anomaly_wagon = data.apply(max, axis=0).idxmax()
# Выбор даты с аномальной температурой
anomaly_date = df.loc[data[anomaly_wagon].idxmax(), 'Дата']
result = pd.DataFrame({'Вагон': [anomaly_wagon], 'Дата': [anomaly_date]})
print(result)
