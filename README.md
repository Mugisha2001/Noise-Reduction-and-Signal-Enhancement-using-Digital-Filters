Objective
The aim of this project is to design and implement digital filters to reduce noise and enhance the clarity of audio signals using Finite Impulse Response (FIR), Infinite Impulse Response (IIR), and adaptive filters. This provides a practical approach to understanding Digital Signal Processing (DSP) techniques.

Description
This project applies digital filters to noisy audio signals to remove unwanted noise and improve signal quality. Filters designed include:

FIR Filters: Known for their stability and linear phase response, used for consistent noise removal.
IIR Filters: Computationally efficient but may introduce phase distortion.
Adaptive Filters (LMS): Dynamically adjust their parameters to handle non-stationary noise.
Using Python and MATLAB, we explore each filter's characteristics and effectiveness in processing audio signals.

Required Libraries (Python)
numpy: Numerical computations.
scipy: Signal processing and filter design.
matplotlib: Visualization of results.
soundfile: Handling audio file operations.
Installation Command:

bash
pip install numpy scipy matplotlib soundfile
Implementation Details
Audio Input: Import or synthesize a noisy signal.
Filter Design: Design FIR, IIR, and LMS adaptive filters.
Noise Reduction: Apply filters to the noisy signal.
Comparison: Evaluate filter performance through visual plots and statistical measures.
Python Implementation
The following Python script demonstrates the filter design and implementation.

python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

# Load audio file
audio, sample_rate = sf.read('noisy_audio.wav')
time = np.arange(audio.shape[0]) / sample_rate

# Add synthetic noise (optional)
noise = 0.02 * np.random.normal(size=audio.shape)
noisy_signal = audio + noise

# FIR Filter
numtaps = 101
cutoff = 0.1
fir_coeff = signal.firwin(numtaps, cutoff)
filtered_signal_fir = signal.lfilter(fir_coeff, 1.0, noisy_signal)

# IIR Filter (Butterworth)
order = 4
b, a = signal.butter(order, cutoff)
filtered_signal_iir = signal.lfilter(b, a, noisy_signal)

# LMS Adaptive Filter
def lms_filter(noisy_signal, desired_signal, mu=0.01, numtaps=32):
    n = len(noisy_signal)
    w = np.zeros(numtaps)
    filtered_signal = np.zeros(n)
    for i in range(numtaps, n):
        x = noisy_signal[i - numtaps:i]
        y = np.dot(w, x)
        error = desired_signal[i] - y
        w += 2 * mu * error * x
        filtered_signal[i] = y
    return filtered_signal

filtered_signal_adaptive = lms_filter(noisy_signal, audio)

# Plot results
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal_fir, label="FIR Filtered")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal_iir, label="IIR Filtered")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal_adaptive, label="Adaptive Filtered")
plt.legend()

plt.show()
MATLAB Implementation
Code:
The MATLAB implementation follows similar steps to Python but uses built-in DSP functions.

% Load an audio file
[audio, Fs] = audioread('noisy_audio.wav');
t = (0:length(audio)-1) / Fs;

% Add synthetic noise
noise = 0.05 * randn(size(audio));  
noisy_signal = audio + noise;

% FIR Filter
fir_order = 50;
fir_cutoff = 0.2;
fir_coeff = fir1(fir_order, fir_cutoff, 'low');
filtered_signal_fir = filter(fir_coeff, 1, noisy_signal);

% IIR Filter
iir_order = 4;
[b, a] = butter(iir_order, fir_cutoff, 'low');
filtered_signal_iir = filter(b, a, noisy_signal);

% LMS Adaptive Filter
lms_mu = 0.01;
lms_order = 32;
lms_filter = dsp.LMSFilter('Length', lms_order, 'StepSize', lms_mu);
[filtered_signal_adaptive, ~] = lms_filter(noisy_signal, audio);

% Plot Results
figure;
subplot(3, 1, 1); plot(t, noisy_signal); title('Noisy Signal');
subplot(3, 1, 2); plot(t, filtered_signal_fir); title('FIR Filtered Signal');
subplot(3, 1, 3); plot(t, filtered_signal_adaptive); title('Adaptive Filtered Signal');
Real-World Applications
Telecommunications: Noise reduction in voice communication.
Audio Engineering: Enhancing audio recordings.
Medical Diagnostics: Filtering noise from ECG or EEG signals.
Environmental Monitoring: Processing sensor data for clearer analysis.
How to Use This Project
Clone the repository from GitHub.
Install dependencies.
Use the Python or MATLAB code in the respective sections.
Replace the sample noisy audio file with your audio file for testing.
