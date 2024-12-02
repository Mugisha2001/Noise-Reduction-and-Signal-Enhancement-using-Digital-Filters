% Load an audio file (replace 'audio.wav' with your actual audio file path)
[audio, Fs] = audioread('C:\Users\educa\Music\HEMBURA_-_James_&_Daniella___Official_Music_Video_+_Live_recorded_at_Kigali__Arena(256k).mp3');  %you may replace your Audio file source
t = (0:length(audio)-1) / Fs; % Time vector

% If audio is stereo, convert it to mono
if size(audio, 2) > 1
    audio = mean(audio, 2);  % Convert stereo to mono (average both channels)
end

% Add synthetic white noise to the audio signal for testing
noise = 0.05 * randn(size(audio));  
noisy_signal = audio + noise;

% Ensure the noisy_signal is also a column vector
noisy_signal = noisy_signal(:);

% Plot the noisy signal
figure;
plot(t, noisy_signal);
title('Noisy Signal');
xlabel('Time (s)');
ylabel('Amplitude');

%% FIR Filter Implementation
% Define FIR filter parameters
fir_order = 50;           % Filter order
fir_cutoff = 0.2;         % Normalized cutoff frequency (cutoff/Nyquist)

% Design the FIR filter
fir_coeff = fir1(fir_order, fir_cutoff, 'low'); 
filtered_signal_fir = filter(fir_coeff, 1, noisy_signal);

% Plot FIR filtered signal
figure;
plot(t, filtered_signal_fir);
title('FIR Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');

%% IIR Filter Implementation
% Define IIR filter parameters
iir_order = 4;            % Filter order for IIR
iir_cutoff = 0.2;         % Normalized cutoff frequency

% Design the IIR Butterworth low-pass filter
[b, a] = butter(iir_order, iir_cutoff, 'low'); 

% Apply the IIR filter
filtered_signal_iir = filter(b, a, noisy_signal);

% Plot IIR filtered signal
figure;
plot(t, filtered_signal_iir);
title('IIR Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');

%% Adaptive Filter (LMS) Implementation
% Adaptive Filter Parameters
lms_mu = 0.01;                    % Step size (learning rate)
lms_order = 32;                   % Order of the adaptive filter
lms_filter = dsp.LMSFilter('Length', lms_order, 'StepSize', lms_mu);

% Apply LMS adaptive filter
[filtered_signal_adaptive, ~] = lms_filter(noisy_signal, audio);

% Plot Adaptive filtered signal
figure;
plot(t, filtered_signal_adaptive);
title('Adaptive (LMS) Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');

%% Comparison of All Filtered Outputs
figure;
subplot(4, 1, 1);
plot(t, noisy_signal);
title('Noisy Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(4, 1, 2);
plot(t, filtered_signal_fir);
title('FIR Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(4, 1, 3);
plot(t, filtered_signal_iir);
title('IIR Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(4, 1, 4);
plot(t, filtered_signal_adaptive);
title('Adaptive (LMS) Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');









