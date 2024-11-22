import numpy as np
import imageio
import sys
import os
def magnify(image, which_bit, folder_from, folder_to):
    if not os.path.exists(os.path.abspath(os.getcwd())+"/"+folder_to):
        os.makedirs(os.path.abspath(os.getcwd())+"/"+folder_to)
    img = imageio.imread(f"{folder_from}/{image}")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    mask = 1 << (int(which_bit)-1)
    for r in range(height):
        for c in range(width):
            if ((img[r, c][0] & mask) >> (int(which_bit)-1)) == 1:
                img[r, c][0] = 0b11111111
            else:
                img[r, c][0] = 0
            if ((img[r, c][1] & mask) >> (int(which_bit)-1)) == 1:
                img[r, c][1] = 0b11111111
            else:
                img[r, c][1] = 0
            if ((img[r, c][2] & mask) >> (int(which_bit)-1)) == 1:
                img[r, c][2] = 0b11111111
            else:
                img[r, c][2] = 0
                
    print(f"{folder_to}/{image.partition("/")[0].partition(".")[0]}")
    imageio.imwrite(f"{folder_to}/{image.partition("/")[0].partition(".")[0]}.png", img)

if __name__ == "__main__":
    magnify(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])