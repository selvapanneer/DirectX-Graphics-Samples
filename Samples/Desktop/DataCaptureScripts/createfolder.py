# Creates 256 folders with folder name 0 to 255
import os

for i in range(256):
    os.makedirs(f"{i}", exist_ok=True)