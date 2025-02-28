import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_data():
  script_dir = os.path.dirname(__file__)
  csv_path = os.path.join(script_dir, 'q4.csv')
  jpg_path = os.path.join(script_dir, 'q4.jpg')

  df = pd.read_csv(csv_path)

  df.index = ['p1', 'p2', 'p3', 'p4', 'p5']

  total_sum = df.values.sum()
  diag_sum = sum(df.iloc[i, i] for i in range(5))
  accuracy = diag_sum / total_sum

  #描画
  plt.figure(figsize=(6, 5))
  sns.heatmap(df, annot=True, fmt='d', cmap='Blues')
  plt.title("Confusion Matrix")
  plt.tight_layout()

  plt.savefig(jpg_path)
  plt.show()

def main():
  plot_data()

if __name__ == '__main__':
  main()
