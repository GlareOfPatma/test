import pandas as pd
from matplotlib import pyplot as plt
from pyod.models.knn import KNN

df = pd.read_excel('1.xlsx')
mas = df.to_numpy()
mas = mas[:len(mas) - 1]
mas = mas[:, 1:9]
ymas = []
averagemas = []
for i in range(len(mas)):
    count = 0
    for j in range(8):
        count += mas[i][j]
    averagemas.append(count / 8)

for i in range(len(mas)):
    ymas.append(i)

clf_name = 'KNN'
clf = KNN()
clf.fit(mas)

y_train_pred = clf.labels_
y_train_score = clf.decision_scores_

y_test_pred = clf.predict(mas)
y_test_score = clf.decision_function(mas)

print(len(y_test_pred), len( ymas))

plt.scatter(ymas, y_test_pred, c = '#FF0000')
plt.scatter(ymas, y_test_score)
plt.scatter(ymas, averagemas, c ="#008000")

plt.show()
