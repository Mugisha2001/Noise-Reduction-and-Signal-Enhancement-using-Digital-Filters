# Noise-Reduction-and-Signal-Enhancement-using-Digital-Filters
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
