import numpy as np
import imageio
import sys
import os
import get_text
from os import listdir
# get the path/directory
if __name__ == "__main__":
    folder_dir = "/Users/mthiessen/COSC383/project4_stego/p4_stego/Images"
    for images in os.listdir(folder_dir):
        print(images)
        print("First 32 bits...")
        get_text.get_header("Images/"+images, 0, 32, 1, 1, 1, 1, "lrtb")
        print("Next 32 bits...")
        get_text.get_header("Images/"+images, 32, 64, 1, 1, 1, 1, "lrtb")


