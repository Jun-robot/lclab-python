import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import os
def plot(valueX, valueY, nameX, nameY, title, save_path):
    plt.figure(figsize=(8, 4))
    plt.plot(valueX, valueY, color='blue')
    plt.title(title)
    plt.xlabel(nameX)
    plt.ylabel(nameY)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    # plt.show()
    plt.close()

def plot_signal():
  script_dir = os.path.dirname(__file__)
  csv_path = os.path.join(script_dir, 'q5.csv')
  jpg1_path = os.path.join(script_dir, 'q5_1.jpg')
  jpg2_path = os.path.join(script_dir, 'q5_2.jpg')
  jpg3_path = os.path.join(script_dir, 'q5_3.jpg')
  jpg4_path = os.path.join(script_dir, 'q5_4.jpg')
  jpg5_path = os.path.join(script_dir, 'q5_5.jpg')

  data = pd.read_csv(csv_path)
  time = data['Time'].values
  amplitude = data['Amplitude'].values

  # original signal
  plot(time, amplitude, 'time', 'amplitude', 'original_signal', jpg1_path)

  # トレンド除去
  amplitude_detrend = signal.detrend(amplitude)
  plot(time, amplitude_detrend, 'time', 'amplitude', 'detrended_signal', jpg2_path)

  # 窓
  winds = np.hanning(len(amplitude_detrend))
  amplitude_windowed = amplitude_detrend * winds
  # plot(time, amplitude_windowed, 'time', 'amplitude', 'windowed_signal', jpg2_path)
  
  #fft
  N = len(amplitude_windowed)
  fft_data = np.fft.fft(amplitude_windowed)
  freq = np.fft.fftfreq(N, d=1.0/1000)
  
  plot(freq[:N//2], np.abs(fft_data)[:N//2], 'frequency', 'magnitude', 'fft', jpg3_path)

  # ローパスフィルタ
  threshold = 0.10 * np.max(np.abs(fft_data))
  fft_data_filtered = fft_data.copy()
  fft_data_filtered[np.abs(fft_data) < threshold] = 0

  plot(freq[:N//2], np.abs(fft_data_filtered)[:N//2], 'frequency', 'magnitude', 'fft_filtered', jpg4_path)

  # 逆フーリエ変換
  amplitude_filtered = np.real(np.fft.ifft(fft_data_filtered))

  #被せて描画
  plt.figure(figsize=(8, 4))
  plt.plot(time, amplitude, color='blue', label='original')
  plt.plot(time, amplitude_filtered, color='red', label='filtered')

  plt.title('original and filtered signal')
  plt.xlabel('time[s]')
  plt.ylabel('amplitude')
  plt.grid(True)
  plt.tight_layout()
  plt.legend()
  plt.savefig(jpg5_path)
  plt.close()


def main():
  plot_signal()

if __name__ == '__main__':
  main()