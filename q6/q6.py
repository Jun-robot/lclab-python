import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import os

def plot_data():
  script_dir = os.path.dirname(__file__)
  csv_path = os.path.join(script_dir, 'q6.csv')
  jpg_path = os.path.join(script_dir, 'q6.jpg')

  df = pd.read_csv(csv_path)
  features = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
  
  pca = PCA(n_components=2)
  pca_result = pca.fit_transform(features)

  df['PC1'] = pca_result[:, 0]
  df['PC2'] = pca_result[:, 1]

  plt.figure(figsize=(8, 6))

  colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}

  for species, color in colors.items():
    subset = df[df['species'] == species]
    plt.scatter(subset['PC1'], subset['PC2'], c=color, label=species)

  plt.title('PCA of Iris Dataset')
  plt.xlabel('PC1')
  plt.ylabel('PC2')
  plt.legend()
  plt.grid()
  plt.savefig(jpg_path)
  plt.show()
  plt.close()

def main():
  plot_data()

if __name__ == '__main__':
  main()