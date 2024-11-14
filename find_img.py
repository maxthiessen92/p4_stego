import numpy as np
import imageio
import sys
if __name__ == "__main__":
    img = imageio.imread(sys.argv[1])
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    lsbs = (1 << int(sys.argv[4])) - 1
    bits = ""
    red = bool(int(sys.argv[5]))
    green = bool(int(sys.argv[6]))
    blue = bool(int(sys.argv[7]))
    orientation = sys.argv[8].lower()
    color_order = sys.argv[9].lower()
    bits_needed = (int(sys.argv[2]) * int(sys.argv[3]) * 3 * 8 + 64)
    print("bits needed: ", bits_needed)
    if orientation == "lrtb":
        for r in range(height):
            for c in range(width):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits += (bin((img[r,c,0] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits+=(bin((img[r,c,1] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits+=(bin((img[r,c,2] & lsbs))[2:].zfill(int(sys.argv[4])))
    elif orientation == "tblr":
        for c in range(height):
            for r in range(width):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits+=(bin((img[r,c,0] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits+=(bin((img[r,c,1] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits+=(bin((img[r,c,2] & lsbs))[2:].zfill(int(sys.argv[4])))
    elif orientation == "btlr":
        for c in range(height-1, -1, -1):
            for r in range(width):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits+=(bin((img[r,c,0] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits+=(bin((img[r,c,1] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits+=(bin((img[r,c,2] & lsbs))[2:].zfill(int(sys.argv[4])))
    elif orientation == "rlbt":
        for c in range(height-1, -1, -1):
            for r in range(width-1, -1, -1):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits+=(bin((img[r,c,0] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits+=(bin((img[r,c,1] & lsbs))[2:].zfill(int(sys.argv[4])))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits+=(bin((img[r,c,2] & lsbs))[2:].zfill(int(sys.argv[4])))
    bits = bits[64:]
    print("Number of bits: ", len(bits))
    image = np.zeros((int(sys.argv[2]), int(sys.argv[3]), 3), dtype=np.uint8)
    for r in range(int(sys.argv[2])):
        for c in range(int(sys.argv[3])):
            if color_order == "rgb":
                if len(bits) >= 8:
                    image[r, c][0] = int(bits[:8], 2)
                    bits = bits[8:]
                else:
                    image[r, c][0] = 0
                if len(bits) >= 8:
                    image[r, c][1] = int(bits[:8], 2)
                    bits = bits[8:]
                else:
                    image[r, c][1] = 0
                if len(bits) >= 8:
                    image[r, c][2] = int(bits[:8], 2)
                    bits = bits[8:]
                else:
                    image[r, c][2] = 0
            elif color_order == "bgr":
                if len(bits) >= 8:
                    image[r, c][2] = int(bits[:8], 2)
                    bits = bits[8:]
                else:
                    image[r, c][2] = 0
                if len(bits) >= 8:
                    image[r, c][1] = int(bits[:8], 2)
                    bits = bits[8:]
                else:
                    image[r, c][1] = 0
                if len(bits) >= 8:
                    image[r, c][0] = int(bits[:8], 2)
                    bits = bits[8:]
                else:
                    image[r, c][0] = 0

    imageio.imwrite("Hidden/"+sys.argv[1][7:], image)
                           
