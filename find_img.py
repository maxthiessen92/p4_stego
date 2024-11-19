import numpy as np
import imageio
import sys

def find_img(i, h, w, depth, rd, gr, bl, orient, color_ord, folder, start_bit):
    img = imageio.imread(i)
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    lsbs = ((1 << int(depth)) - 1) << (int(start_bit)-1)
    bits = ""
    red = bool(int(rd))
    green = bool(int(gr))
    blue = bool(int(bl))
    orientation = orient.lower()
    color_order = color_ord.lower()
    bits_needed = ((int(h) * int(w) * 3 * 8) + 64)
    print("bits needed: ", bits_needed)
    if orientation == "lrtb":
        for r in range(height):
            for c in range(width):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits += (bin(((img[r,c,0] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits += (bin(((img[r,c,1] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits += (bin(((img[r,c,2] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
    elif orientation == "tblr":
        for c in range(height):
            for r in range(width):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits += (bin(((img[r,c,0] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits += (bin(((img[r,c,1] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits += (bin(((img[r,c,2] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
    elif orientation == "btlr":
        for c in range(height-1, -1, -1):
            for r in range(width):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits += (bin(((img[r,c,0] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits += (bin(((img[r,c,1] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits += (bin(((img[r,c,2] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
    elif orientation == "rlbt":
        for c in range(height-1, -1, -1):
            for r in range(width-1, -1, -1):
                if len(bits) < bits_needed:
                    if len(bits) == bits_needed:
                        break
                    if red:
                        bits += (bin(((img[r,c,0] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if green:
                        bits += (bin(((img[r,c,1] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
                    if len(bits) == bits_needed:
                        break
                    if blue:
                        bits += (bin(((img[r,c,2] & lsbs) >> (int(start_bit)-1)))[2:].zfill(int(depth)))
    bits = bits[64:]
    print("Number of bits: ", len(bits)+64)
    image = np.zeros((int(h), int(w), 3), dtype=np.uint8)
    for r in range(int(h)):
        for c in range(int(w)):
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

    imageio.imwrite(folder+"/"+i.partition("/")[-1], image)
if __name__ == "__main__":
    find_img(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11])
