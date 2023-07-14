import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes




with open("C:\Users\flipk\Downloads\header.txt", "rb") as f:
    byte = f.read(8)
    while byte != b"":
        # Do stuff with byte.
        print(byte)
        print(len(byte))
        byte = f.read(8)
    print(byte)