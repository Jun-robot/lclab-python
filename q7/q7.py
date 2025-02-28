import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import os

def hoge():
  script_dir = os.path.dirname(__file__)
  csv_path = os.path.join(script_dir, '../q6/q6.csv')
  jpg_path = os.path.join(script_dir, 'q7.jpg')

  df = pd.read_csv(csv_path)
  x=df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
  y=df['label']

  kf = KFold(n_splits=5, shuffle=True, random_state=50  )

  y_true_all = []
  y_pred_all = []

  fold = 1
  for train_index, test_index in kf.split(x):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    clf = SVC(kernel='linear', random_state=50)
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    y_true_all.extend(y_test)
    y_pred_all.extend(y_pred)

    cm_fold = confusion_matrix(y_test, y_pred)
    fold += 1

  cm_overall = confusion_matrix(y_true_all, y_pred_all)


  plt.figure(figsize=(10, 7))
  sns.heatmap(cm_overall, annot=True, fmt='d', cmap='Blues',
              xticklabels=['setosa', 'versicolor', 'virginica'],
              yticklabels=['setosa', 'versicolor', 'verginica'])
  plt.xlabel('Predicted Label')
  plt.ylabel('True Label')
  plt.title('Confusion Matrix')
  plt.savefig(jpg_path)
  plt.show()

def main():
  hoge()

if __name__ == '__main__':
  main()