import numpy as np
import imageio
import sys
import os
import get_text
import magnify_lsbs
import find_img
# get the path/directory

def check_all_headers(search, depth, rd, gr, bl, orient, s_bit):
    if not os.path.exists(os.path.abspath(os.getcwd())+f"/ConsoleLogs/{search}"):
        os.makedirs(os.path.abspath(os.getcwd())+f"/ConsoleLogs/{search}")
    log_file_path = os.path.abspath(os.getcwd()) + f"/ConsoleLogs/{search}/header_{orient}_{s_bit}_{depth}_{rd}_{gr}_{bl}.txt"
    with open(log_file_path, 'w') as f:
        original_stdout = sys.stdout  # Save the original stdout
        sys.stdout = f  # Redirect stdout to the file

        try:
            folder_dir = os.path.abspath(os.getcwd()) + f"/{search}"
            for images in os.listdir(folder_dir):
                print(images)
                print("First 32 bits...")
                get_text.get_header(f"{search}/{images}", 0, 32, int(depth), int(rd), int(gr), int(bl), orient, int(s_bit))
                print("Next 32 bits...")
                get_text.get_header(f"{search}/{images}", 32, 64, int(depth), int(rd), int(gr), int(bl), orient, int(s_bit))
        finally:
            sys.stdout = original_stdout  # Restore the original stdout

def create_magnified(bit, folder, search_from):
    if not os.path.exists(os.path.abspath(os.getcwd())+"/"+folder):
        os.makedirs(os.path.abspath(os.getcwd())+"/"+folder)
    folder_dir = os.path.abspath(os.getcwd())+"/"+search_from
    for img in os.listdir(folder_dir):
        magnify_lsbs.magnify("Images/"+img, bit, folder)

def create_hidden_images(img, h, w, depth, rd, gr, bl, orient, color_ord, start_bit):
    if not os.path.exists(os.path.abspath(os.getcwd())+f"/Hidden_{orient}_{start_bit}_{depth}_{rd}_{gr}_{bl}"):
        os.makedirs(os.path.abspath(os.getcwd())+f"/Hidden_{orient}_{start_bit}_{depth}_{rd}_{gr}_{bl}")
    file_path = os.path.abspath(os.getcwd())+f"/Hidden_{orient}_{start_bit}_{depth}_{rd}_{gr}_{bl}"
    find_img.find_img(img, h, w, depth, rd, gr, bl, orient, color_ord, file_path, start_bit)

if __name__ == "__main__":
    exit = 0
    while not exit:
        print("Choose an operation (1,2,3, etc.):\n1. Check headers\n2. Magnify LSB\n3. Generate hidden images\n4. Quit")
        choice = int(input())
        
        match choice:
            case 1:
                search = input("What folder do you want to iterate through?: ")
                depth = input("Enter number of lsbs you want to check: ")
                r = input("Check red channel? (1 or 0): ")
                g = input("Check green channel? (1 or 0): ")
                b = input("Check blue channel? (1 or 0): ")
                orient = input("What orientation do you want to search by? (lrtb, tblr, etc.): ")
                s_bit = input("What LSB do you want to start at? (1-8): ")
                check_all_headers(search, depth, r, g, b, orient, s_bit)
            case 2:
                bit = input("What bit do you want to  magnify?: ")
                folder = input("Name of folder to save to: ")
                create_magnified(bit, folder)
            case 3:
                search = input("What folder are you searching from?:")
                img = input("Image name:")
                height = input("Image height: ")
                width = input("Image width: ")
                depth = input("Enter number of lsbs you want to check: ")
                r = input("Check red channel? (1 or 0): ")
                g = input("Check green channel? (1 or 0): ")
                b = input("Check blue channel? (1 or 0): ")
                orient = input("What orientation do you want to search by? (lrtb, tblr, etc.): ")
                color_ord = input("What color order do you want? (rgb, bgr, etc.?):")
                s_bit = input("What LSB do you want to start at? (1-8): ")
                create_hidden_images(search+"/"+img, height, width, depth, r, g, b, orient, color_ord, s_bit)
            case 4:
                exit = 1
            case _:
                print("Pick a proper option")
    

    
    
    # if not os.path.exists():
        


