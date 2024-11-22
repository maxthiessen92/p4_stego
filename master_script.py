import numpy as np
import imageio
import sys
import os
import get_text
import magnify_lsbs
import find_img
from multiprocessing import Pool, cpu_count
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
def check_header(search, img, depth, rd, gr, bl, orient, s_bit):
    print(img)
    print("First 32 bits...")
    dims, first = get_text.get_header(f"{search}/{img}", 0, 32, int(depth), int(rd), int(gr), int(bl), orient, int(s_bit))

    print("Next 32 bits...")
    _, second = get_text.get_header(f"{search}/{img}", 32, 64, int(depth), int(rd), int(gr), int(bl), orient, int(s_bit))

    return (dims, first, second)
        
def create_magnified(bit, search_from, send_to):
    if not os.path.exists(os.path.abspath(os.getcwd())+"/"+send_to):
        os.makedirs(os.path.abspath(os.getcwd())+"/"+send_to)
    folder_dir = os.path.abspath(os.getcwd())+"/"+search_from
    for img in os.listdir(folder_dir):
        magnify_lsbs.magnify(f"{img}", bit, search_from, send_to)

def create_headers_for_image(image, folder):
    if not os.path.exists(os.path.abspath(os.getcwd())+f"/{image.partition('.')[0]}"):
        os.makedirs(os.path.abspath(os.getcwd())+f"/{image.partition('.')[0]}")
            
    search = f"{folder}"
    depth_values = range(1, 3)  
    rgb_values = [0, 1]  
    orientations = ["lrtb", "lrbt", "rltb", "rlbt", "tblr", "tbrl", "btlr", "btrl"]  
    start_bits = range(1, 3)  

    # Iterate through all combinations
    for depth in depth_values:
        for r in rgb_values:
            for g in rgb_values:
                for b in rgb_values:
                    if g == 0 and r == 0 and b == 0:
                        continue
                    for orientation in orientations:
                        for start_bit in start_bits:
                            print(f"Start bit: {start_bit} Orientation: {orientation} R:{r} G:{g} B:{b} Depth:{depth}")
                            header_tuple = check_header(search, image, depth, r, g, b, orientation, start_bit)
                            if header_tuple[1] and header_tuple[2]:
                                if header_tuple[1] < header_tuple[0][0] and header_tuple[2] < header_tuple[0][1]:
                                    file_path = os.path.abspath(os.getcwd())+f"/{image.partition('.')[0]}"
                                    find_img.find_img(f"{search}/{image}", header_tuple[1], header_tuple[2], depth, r, g, b, orientation, "rgb", file_path, start_bit)
                                else:
                                    continue
                            elif header_tuple[1]:
                                log_file_path = os.path.abspath(os.getcwd())+f"/{image.partition('.')[0]}/{header_tuple[1]}_{orientation}_{start_bit}_{depth}_{r}_{g}_{b}.txt"
                                with open(log_file_path, 'w') as f:
                                    original_stdout = sys.stdout  # Save the original stdout
                                    sys.stdout = f  # Redirect stdout to the file
                                    get_text.find_message(f"{search}/{image}", 0, int(header_tuple[1])+32, depth, r, g, b, orientation, start_bit)
                                    sys.stdout = original_stdout  # Restore the original stdout
  
def process_image(args):
    """Helper function to process a single image with multiprocessing."""
    image, search_folder = args
    create_headers_for_image(image, search_folder)

def is_valid_image_file(filename):
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    return os.path.splitext(filename.lower())[1] in valid_extensions


def mass_create(search_folder):

    folder_dir = os.path.abspath(os.getcwd()) + f"/{search_folder}"
    images = [img for img in os.listdir(folder_dir) if is_valid_image_file(img)]
    
    # Use multiprocessing to process images in parallel
    with Pool(cpu_count()) as pool:
        pool.map(process_image, [(image, search_folder) for image in images])

def flip_images_in_folder(folder_from, folder_to):
    if not os.path.exists(os.path.abspath(os.getcwd())+"/"+folder_to):
        os.makedirs(os.path.abspath(os.getcwd())+"/"+folder_to)
    folder_dir = os.path.abspath(os.getcwd())+"/"+folder_from
    file_path = os.path.abspath(os.getcwd())+f"/{folder_to}"
    for img in os.listdir(folder_dir):
        if is_valid_image_file(img):
            find_img.flip_image(f"{folder_from}/{img}", file_path)
       
def create_hidden_images(img, h, w, depth, rd, gr, bl, orient, color_ord, start_bit):
    if not os.path.exists(os.path.abspath(os.getcwd())+f"/Hidden_{orient}_{start_bit}_{depth}_{rd}_{gr}_{bl}"):
        os.makedirs(os.path.abspath(os.getcwd())+f"/Hidden_{orient}_{start_bit}_{depth}_{rd}_{gr}_{bl}")
    file_path = os.path.abspath(os.getcwd())+f"/Hidden_{orient}_{start_bit}_{depth}_{rd}_{gr}_{bl}"
    find_img.find_img(img, h, w, depth, rd, gr, bl, orient, color_ord, file_path, start_bit)

if __name__ == "__main__":
    exit = 0
    while not exit:
        print("Choose an operation (1,2,3, etc.):")
        print("1. Check headers\n2. Mass check headers \n3. Check for header of specific image")
        print("4. Look at possible headers of specific Image\n5. Magnify LSB\n6. Generate hidden images")
        print("7. Mass generate text and images from folder\n8. Search for message\n9. Magnify singal image\n10.Flip images in folder\n11.Quit")
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
                search = "Images"
                depth_values = range(1, 3)  
                rgb_values = [0, 1]  
                orientations = ["lrtb", "lrbt", "rltb", "rlbt", "tblr", "tbrl", "btlr", "btrl"]  
                start_bits = range(1, 3)  

                # Iterate through all combinations
                for depth in depth_values:
                    for r in rgb_values:
                        for g in rgb_values:
                            for b in rgb_values:
                                if g == 0 and r == 0 and b == 0:
                                    continue
                                for orientation in orientations:
                                    for start_bit in start_bits:
                                        print(f"Start bit: {start_bit} Orientation: {orientation} R:{r} G:{g} B:{b} Depth:{depth}")
                                        check_all_headers(search, depth, r, g, b, orientation, start_bit)
            case 3:
                search = input("What folder do you want to iterate through?: ")
                img = input("Image name:")
                orient = input("What orientation do you want to search by? (lrtb, tblr, etc.): ")
                s_bit = input("What LSB do you want to start at? (1-8): ")
                depth = input("Enter number of lsbs you want to check: ")
                r = input("Check red channel? (1 or 0): ")
                g = input("Check green channel? (1 or 0): ")
                b = input("Check blue channel? (1 or 0): ")
                check_header(search, img, depth, r, g, b, orient, s_bit)
            case 4:
                search = input("What folder are you searching from?:")
                img = input("Image name:")
                create_headers_for_image(img, search)
            case 5:
                bit = input("What bit do you want to  magnify?: ")
                folder = input("What folder are you searching through: ")
                save_to = input("Name of folder to save to: ")
                create_magnified(bit, folder, save_to)
            case 6:
                search = input("What folder are you searching from?:")
                img = input("Image name:")
                height = input("Image height: ")
                width = input("Image width: ")
                orient = input("What orientation do you want to search by? (lrtb, tblr, etc.): ")
                s_bit = input("What LSB do you want to start at? (1-8): ")
                depth = input("Enter number of lsbs you want to check: ")
                r = input("Check red channel? (1 or 0): ")
                g = input("Check green channel? (1 or 0): ")
                b = input("Check blue channel? (1 or 0): ")
                color_ord = input("What color order do you want? (rgb, bgr, etc.?):")
                
                create_hidden_images(search+"/"+img, height, width, depth, r, g, b, orient, color_ord, s_bit)
            case 7:
                search = input("What folder are you searching from?:")
                mass_create(search)
            case 8:
                search = input("What folder do you want to iterate through?: ")
                img = input("Image name:")
                header_end = input("What bit does the header end?:")
                length = input("message length: ")
                orient = input("What orientation do you want to search by? (lrtb, tblr, etc.): ")
                s_bit = input("What LSB do you want to start at? (1-8): ")
                depth = input("Enter number of lsbs you want to check: ")
                r = input("Check red channel? (1 or 0): ")
                g = input("Check green channel? (1 or 0): ")
                b = input("Check blue channel? (1 or 0): ")
               
                get_text.find_message(f"{search}/{img}", header_end, int(length)+32, depth, r, g, b, orient, s_bit)   
            case 9:
                search = input("What folder is the image you want to magnify in?: ")
                img = input("Image name:")
                save_to = input("What folder do you want to save to?:")
                bit = input("What bit do you want to magnify:")
                magnify_lsbs.magnify(img, bit, search, save_to)
            case 10:
                search = input("What folder are the images you want to flip in?: ")
                save_to = input("What folder do you want to save to?:")
                flip_images_in_folder(search, save_to)
            case 11:
                exit = 1
            case _:
                print("Pick a proper option")



