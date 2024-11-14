import numpy as np
import imageio
import sys
if __name__ == "__main__":
    img = imageio.imread(sys.argv[1])
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)

    if sys.argv[2] == 'r':
        for r in range(height):
            for c in range(width):
                img[r, c][0] = img[r, c, 0]
                img[r, c][1] = 120
                img[r, c][2] = 0
    elif sys.argv[2] == 'g':
        for r in range(height):
            for c in range(width):
                img[r, c][0] = 120
                img[r, c][1] = img[r, c, 1]
                img[r, c][2] = 0
    else:
        for r in range(height):
            for c in range(width):
                img[r, c][0] = 120
                img[r, c][1] = 0
                img[r, c][2] = img[r, c, 2]
imageio.imwrite("ColorShift/"+sys.argv[2]+"_"+sys.argv[1][7:], img)