import os

def menu():
    os.system('clear')
    print("Welcome to the fourier program, please choose an option:")
    print("a)... Create a new signal")
    print("b)... Mix Signals")
    print("c)... Generate the FFT")
    print("d)... Inverse FFT")
    print("e)... Exit")
    choose = input("Option: ")
    return choose