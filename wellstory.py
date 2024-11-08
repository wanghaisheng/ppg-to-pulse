import numpy as np
import matplotlib.pyplot as plt
import pywt
import pandas as pd
from scipy.fft import fft, fftfreq

# Load PPG signal from CSV file
# Replace 'PPG.csv' with the path to your actual CSV file
data = pd.read_csv("PPG.csv")

# Inspect the first few rows to confirm the structure of the data
print(data.head())

# Extract the time and Red channel (R) for the PPG signal
time = data['time'].values  # Time column (in seconds)
ppg_signal = data['R'].values  # Using the 'R' column for the PPG signal

# Define the sampling frequency (fs)
# If the time is given in seconds, fs is the inverse of the time difference between consecutive samples.
# For example:
fs = 1 / np.mean(np.diff(time))  # Sampling frequency in Hz, based on the time column

# Perform 8-level wavelet decomposition using the sym8 wavelet
wavelet = 'sym8'
level = 8
coeffs = pywt.wavedec(ppg_signal, wavelet, level=level)

# Function to compute the dominant frequency of a signal using FFT
def dominant_frequency(signal, fs):
    # Apply FFT
    N = len(signal)
    freqs = fftfreq(N, d=1/fs)
    fft_vals = fft(signal)
    
    # Only keep the positive frequencies
    pos_freqs = freqs[freqs > 0]
    pos_fft_vals = np.abs(fft_vals[freqs > 0])
    
    # Find the frequency with the highest amplitude
    dominant_freq = pos_freqs[np.argmax(pos_fft_vals)]
    return dominant_freq

# Step 1: Calculate the dominant frequency for each decomposition level
dominant_freqs = []
for i in range(1, level + 1):
    coeff = coeffs[i]  # Get the detail coefficients for each level
    dominant_freq = dominant_frequency(coeff, fs)  # Compute the dominant frequency
    dominant_freqs.append(dominant_freq)  # Store the dominant frequencies
    print(f"Level {i} - Dominant Frequency: {dominant_freq:.2f} Hz")
    
# Step 2: Identify the level with the lowest dominant frequency (most likely baseline drift)
baseline_level = np.argmin(dominant_freqs) + 1  # Adding 1 since levels start from 1
print(f"\nMost probable baseline drift level: Level {baseline_level} with dominant frequency of {dominant_freqs[baseline_level-1]:.2f} Hz")

# Step 3: Zero out the coefficients at the most probable baseline drift level
coeffs[baseline_level] = np.zeros_like(coeffs[baseline_level])  # Set coefficients of the baseline drift level to zero

# Step 4: Reconstruct the signal with the modified coefficients
reconstructed_signal = pywt.waverec(coeffs, wavelet)

# Step 5: Plot the original and processed (baseline drift removed) signals
plt.figure(figsize=(10, 6))
plt.plot(time, ppg_signal, label='Original Signal')
plt.plot(time, reconstructed_signal, label='Processed Signal (Baseline Drift Removed)', linestyle='--')
plt.title("PPG Signal: Original vs Processed (Baseline Drift Removed)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Optionally, you can save the processed signal to a new CSV file
# pd.DataFrame({'Time': time, 'Processed PPG': reconstructed_signal}).to_csv("processed_PPG.csv", index=False)
