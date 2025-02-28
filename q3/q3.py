import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_data():
  script_dir = os.path.dirname(__file__)
  csv_pathA = os.path.join(script_dir, 'q3_dataA.csv')
  csv_pathB = os.path.join(script_dir, 'q3_dataB.csv')
  jpg_path = os.path.join(script_dir, 'q3.jpg')

  dataA = pd.read_csv(csv_pathA)
  dataB = pd.read_csv(csv_pathB)

  fig = plt.figure(figsize=(12, 8))

  # Plot dataA
  ax1 = fig.add_subplot(2, 2, 1)
  ax1.plot(dataA['People'], dataA['Weight'], marker='o', color='blue', label='weight')
  ax1.set_title('Weights')
  ax1.set_xlabel('People')
  ax1.set_ylabel('Weight')
  ax1.set_ylim(0, 100)
  ax1.grid(True)
  ax1.legend()

  # Plot dataB
  ax2 = fig.add_subplot(2, 2, 2)
  ax2.bar(dataB['People'], dataB['Year'], color='orange', label='year')
  ax2.set_title('Years')
  ax2.set_xlabel('People')
  ax2.set_ylabel('Year')
  ax2.set_ylim(1970, 2020)
  ax2.grid(True)
  ax2.legend()

  # Plot dataA and dataB
  ax3 = fig.add_subplot(2, 1, 2)

  # left: Plot dataA
  ax3.plot(dataA['People'], dataA['Weight'], marker='o', color='blue', label='weight')
  ax3.set_title('Weights and Years')
  ax3.set_xlabel('People')
  ax3.set_ylabel('Weight')
  ax3.set_ylim(0, 100)
  ax3.grid(True)
  
  # right: Plot dataB
  ax4 = ax3.twinx()
  ax4.bar(dataB['People'], dataB['Year'], color='orange', alpha=0.7, label='year')
  ax4.set_ylabel('Year')
  ax4.set_ylim(1970, 2020)

  ax3.legend(loc='upper left')
  ax4.legend(loc='upper right')

  plt.tight_layout()
  plt.savefig(jpg_path)
  plt.show()

def main():
  plot_data()

if __name__ == '__main__':
  main()