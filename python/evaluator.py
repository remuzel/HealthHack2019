import numpy as np
from matplotlib import pyplot as plt 
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections

def categorize(segment):
    p = {
        "00000": ,
        "00001": ,
        "00010": ,
        "00011": ,
        "00100": ,
        "00101": ,
        "00110": ,
        "00111": ,
        "01000": ,
        "01001": ,
        "01010": ,
        "01011": ,
        "01100": ,
        "01101": ,
        "01110": ,
        "01111": ,
        "10000": ,
        "10001": ,
        "10010": ,
        "10011": ,
        "10100": ,
        "10101": ,
        "10110": ,
        "10111": ,
        "11000": ,
        "11001": ,
        "11010": ,
        "11011": ,
        "11100": ,
        "11101": ,
        "11110": ,
        "11111": 
    }
    
    response = p[segment]



def main():
    # segment = [input() for _ in range(5)]
    segment = "10110"
    categorize(segment)

if __name__ == '__main__':
 main()