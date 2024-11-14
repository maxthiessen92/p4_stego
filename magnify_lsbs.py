import numpy as np
import imageio
import sys
if __name__ == "__main__":
    img = imageio.imread(sys.argv[1])
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    for r in range(height):
        for c in range(width):
            if img[r, c][0] & 1 == 1:
                img[r, c][0] = 0b11111111
            else:
                img[r, c][0] = 0
            if img[r, c][1] & 1 == 1:
                img[r, c][1] = 0b11111111
            else:
                img[r, c][1] = 0
            if img[r, c][2] & 1 == 1:
                img[r, c][2] = 0b11111111
            else:
                img[r, c][2] = 0
                

imageio.imwrite("AlteredImages/"+sys.argv[1][7:], img)