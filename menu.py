import os

def menu():
    os.system('clear')
    print("Welcome to the fourier program, please choose an option:")
    print("a)... Create a new signal")
    print("b)... Generate the FFT")
    print("c)... Inverse FFT")
    print("d)... Exit")
    choose = input("Option: ")
    return choose