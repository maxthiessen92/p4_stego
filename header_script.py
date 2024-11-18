import numpy as np
import imageio
import sys
import os
import get_text
import magnify_lsbs
# get the path/directory

def check_all_headers(depth, rd, gr, bl, orient):
    if not os.path.exists(os.path.abspath(os.getcwd())+"/ConsoleLogs"):
        os.makedirs(os.path.abspath(os.getcwd())+"/ConsoleLogs")
    log_file_path = os.path.abspath(os.getcwd()) + f"/ConsoleLogs/header_{depth}_{rd}_{gr}_{bl}_{orient}.txt"
    with open(log_file_path, 'w') as f:
        original_stdout = sys.stdout  # Save the original stdout
        sys.stdout = f  # Redirect stdout to the file

        try:
            folder_dir = os.path.abspath(os.getcwd()) + "/Images"
            for images in os.listdir(folder_dir):
                print(images)
                print("First 32 bits...")
                get_text.get_header(f"Images/{images}", 0, 32, int(depth), int(rd), int(gr), int(bl), orient)
                print("Next 32 bits...")
                get_text.get_header(f"Images/{images}", 32, 64, int(depth), int(rd), int(gr), int(bl), orient)
        finally:
            sys.stdout = original_stdout  # Restore the original stdout

def create_magnified(bit, folder):
    if not os.path.exists(os.path.abspath(os.getcwd())+"/"+folder):
        os.makedirs(os.path.abspath(os.getcwd())+"/"+folder)
    folder_dir = os.path.abspath(os.getcwd())+"/Images"
    for img in os.listdir(folder_dir):
        magnify_lsbs.magnify("Images/"+img, bit, folder)

if __name__ == "__main__":
    exit = 0
    while not exit:
        print("Choose an operation (1,2,3, etc.):\n1. Check headers\n2. Magnify LSB\n3. Quit")
        choice = int(input())
        
        match choice:
            case 1:
                depth = input("Enter number of lsbs you want to check: ")
                r = input("Check red channel? (1 or 0): ")
                g = input("Check green channel? (1 or 0): ")
                b = input("Check blue channel? (1 or 0): ")
                orient = input("What orientation do you want to search by? (lrtb, tblr, etc.): ")
                check_all_headers(depth, r, g, b, orient)
            case 2:
                bit = input("What bit do you want to  magnify?: ")
                folder = input("Name of folder to save to: ")
                create_magnified(bit, folder)
            case 3:
                exit = 1
            case _:
                print("Pick a proper option")
    

    
    
    # if not os.path.exists():
        


