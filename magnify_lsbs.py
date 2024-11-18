import numpy as np
import imageio
import sys
def magnify(image, which_bit, folder):
    img = imageio.imread(image)
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
                

    imageio.imwrite(folder+"/"+image[7:], img)

if __name__ == "__main__":
    magnify(sys.argv[1], sys.argv[2], sys.argv[3])