from scipy.fft import rfft, rfftfreq
import numpy as np
from matplotlib import pyplot as plt
import os
import json

def fastFourier():
    os.system('ls mixed')
    filename = input("Type the name of the mixed signal: ")
    f = open("mixed/"+filename,"r")
    data = f.read()
    data = json.loads(data)
    f.close()
    signal = np.array(data["signal"])
    SAMPLE_RATE = int(data["SampleRate"])
    DURATION = int(data["Duration"])
    N = SAMPLE_RATE * DURATION

    yf = rfft(signal)
    xf = rfftfreq(N, 1 / SAMPLE_RATE)

    plt.plot(xf, np.abs(yf))
    plt.show()