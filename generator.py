import numpy as np
import json
from matplotlib import pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

def generate_signal():
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