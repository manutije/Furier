import os 
import json
import numpy as np
from matplotlib import pyplot as plt

def signalMixer():
    numSignals = int(input("How many signals you want to mix: "))
    os.system('clear')
    print('These are the signals in the database')
    print(os.system('ls signals'))
    signalSMP = input("Type the signal Sample Rate:  ")
    signalDUR = input("Type the signal Duration: ")
    cont = 0
    final = 0 
    while cont <numSignals:
        signalFRE = input("Type the signal Frequency: ")
        signalPWD = float(input("Type the signal Power: "))
        signalName = "SMP"+signalSMP+"DUR"+signalDUR+"FRE"+signalFRE+'.sig'
        f = open("signals/"+signalName,"r")
        data = f.read()
        data = json.loads(data)
        f.close()
        y_value = np.array(data["y"])
        y_value = y_value * signalPWD
        final = final + y_value
        cont = cont + 1
    normalized_tone = np.int16((final / final.max()) * 32767)
    plt.plot(final[:1000])
    plt.show()
    save = input("Do you want to save the new mixed signal [y/n]: ").lower()
    if save == 'y':
        name = input("Type the name of the new mixed signal: ")
        signal = {
            "SampleRate":signalSMP,
            "Duration":signalDUR,
            "signal":normalized_tone.tolist()
        }
        f=open("mixed/"+name+'.mix',"w")
        f.write(json.dumps(signal))
        f.close()
