# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft
from generator import generate_sine_wave
from menu import menu
import os
import json

choose = 'z'

while choose != 'd':
    choose = menu().lower()

    if choose =='a':
        
        os.system('clear')
        SAMPLE_RATE = int(input("Please type a sample rate: "))
        DURATION = int(input("Please type the duration: "))
        FRECUENCY = int(input("Please type the frecuency: "))

        new_tone_x, new_tone_y = generate_sine_wave(FRECUENCY, SAMPLE_RATE, DURATION)

        plt.plot(new_tone_x[:1000],new_tone_y[:1000])
        plt.show()

        save = input("Do you want to save the new signal [y/n]: ").lower()
        if save == 'y':
            name = 'SMP'+str(SAMPLE_RATE)+'DUR'+str(DURATION)+'FRE'+str(FRECUENCY)
            signal = {
                "SampleRate":SAMPLE_RATE,
                "Duration":DURATION,
                "Frecuency":FRECUENCY,
                "x":new_tone_x.tolist(),
                "y":new_tone_y.tolist()
            }
            f=open("signals/"+name+'.sig',"w")
            f.write(json.dumps(signal))
            f.close()



#Start Variables
SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)

plt.plot(normalized_tone[:1000])
plt.show()

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()

# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)

# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)

yf[target_idx - 1 : target_idx + 2] = 0

plt.plot(xf, np.abs(yf))
plt.show()

new_sig = irfft(yf)

plt.plot(new_sig[:1000])
plt.show()

norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
write("clean.wav", SAMPLE_RATE, norm_new_sig)
