# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

# Load an audio file (replace 'noisy_audio.wav' with your file path)
audio, sample_rate = sf.read('noisy_audio.wav')

# If the audio is stereo, convert it to mono
if len(audio.shape) > 1:
    audio = np.mean(audio, axis=1)

# Normalize the audio for consistency
audio = audio / np.max(np.abs(audio))

# Create a time vector for plotting
time = np.arange(audio.shape[0]) / sample_rate

# Add synthetic white noise to the audio
noise = 0.05 * np.random.normal(size=audio.shape)
noisy_signal = audio + noise

# Plot the original and noisy signals
plt.figure(figsize=(10, 4))
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, audio, label="Original Signal")
plt.legend()
plt.title("Original vs. Noisy Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# ------------------------------------
# FIR Filter Implementation
# ------------------------------------
# Define FIR filter parameters
numtaps = 101  # Filter order
cutoff = 0.1   # Normalized cutoff frequency (cutoff/Nyquist)

# Design the FIR filter
fir_coeff = signal.firwin(numtaps, cutoff, pass_zero="lowpass")

# Apply the FIR filter to the noisy signal
filtered_signal_fir = signal.lfilter(fir_coeff, 1.0, noisy_signal)

# Plot the FIR filtered signal
plt.figure(figsize=(10, 4))
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal_fir, label="FIR Filtered Signal", color='green')
plt.legend()
plt.title("FIR Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# ------------------------------------
# IIR Filter Implementation
# ------------------------------------
# Define IIR filter parameters
order = 4
cutoff = 0.1  # Normalized cutoff frequency

# Design the IIR Butterworth low-pass filter
b, a = signal.butter(order, cutoff, btype='low')

# Apply the IIR filter to the noisy signal
filtered_signal_iir = signal.lfilter(b, a, noisy_signal)

# Plot the IIR filtered signal
plt.figure(figsize=(10, 4))
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal_iir, label="IIR Filtered Signal", color='orange')
plt.legend()
plt.title("IIR Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# ------------------------------------
# Adaptive Filter Implementation (LMS)
# ------------------------------------
def lms_filter(noisy_signal, desired_signal, mu=0.01, numtaps=32):
    """
    Least Mean Squares (LMS) adaptive filter.
    """
    n = len(noisy_signal)
    w = np.zeros(numtaps)  # Filter weights
    filtered_signal = np.zeros(n)  # Output signal

    # Adaptive filtering process
    for i in range(numtaps, n):
        x = noisy_signal[i - numtaps:i]  # Input signal
        y = np.dot(w, x)  # Filter output
        error = desired_signal[i] - y  # Error signal
        w += 2 * mu * error * x  # Update weights
        filtered_signal[i] = y

    return filtered_signal

# Apply the adaptive filter
filtered_signal_adaptive = lms_filter(noisy_signal, audio)

# Plot the Adaptive filtered signal
plt.figure(figsize=(10, 4))
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal_adaptive, label="Adaptive Filtered Signal", color='red')
plt.legend()
plt.title("Adaptive (LMS) Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# ------------------------------------
# Compare Results
# ------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(time, noisy_signal, label="Noisy Signal", color='blue')
plt.legend()
plt.title("Noisy Signal")

plt.subplot(4, 1, 2)
plt.plot(time, filtered_signal_fir, label="FIR Filtered Signal", color='green')
plt.legend()
plt.title("FIR Filtered Signal")

plt.subplot(4, 1, 3)
plt.plot(time, filtered_signal_iir, label="IIR Filtered Signal", color='orange')
plt.legend()
plt.title("IIR Filtered Signal")

plt.subplot(4, 1, 4)
plt.plot(time, filtered_signal_adaptive, label="Adaptive Filtered Signal", color='red')
plt.legend()
plt.title("Adaptive (LMS) Filtered Signal")

plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.grid()
plt.show()

## Explanation
Load Audio: The soundfile library reads the audio file (noisy_audio.wav). If the audio is stereo, it's converted to mono.
Add Noise: Synthetic white noise is added to simulate a noisy environment.
FIR Filter: A finite impulse response (FIR) filter is applied to remove high-frequency noise.
IIR Filter: An infinite impulse response (IIR) Butterworth filter is used for low-pass filtering.
Adaptive Filter (LMS): Implements a basic Least Mean Squares (LMS) adaptive filter that dynamically adjusts based on input noise.
Results: Each filter's output is plotted for comparison against the noisy signal.

## Requirements
Ensure you have the following Python libraries installed:
pip install numpy scipy matplotlib soundfile
Replace 'noisy_audio.wav' with the path to your audio file for testing. Adjust parameters (e.g., filter order, cutoff frequency) as needed to optimize results for your specific use case.
