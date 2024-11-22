import numpy as np
import imageio
import sys

def find_img(i, h, w, depth, rd, gr, bl, orient, color_ord, folder, start_bit):
    img = imageio.imread(i)
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    lsbs = ((1 << int(depth)) - 1) << (int(start_bit)-1)
    bits = []
    red = bool(int(rd))
    green = bool(int(gr))
    blue = bool(int(bl))
    orientation = orient.lower()
    color_order = color_ord.lower()
    bits_needed = ((int(h) * int(w) * 3 * 8) + 64)
    print("bits needed: ", bits_needed)
    match orientation:
        case "lrtb":
            for r in range(height):
                for c in range(width):
                   if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "rltb":
            for r in range(height):
                for c in range(width - 1, -1, -1):
                   if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "tblr":
            for c in range(height):
                for r in range(height):
                    if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "tbrl":
            for c in range(width - 1, -1, -1):
                for r in range(height):
                    if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "btlr":
            for c in range(width):
                for r in range(height - 1, -1, -1):
                   if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "btrl":
            for c in range(width-1, -1, -1):
                for r in range(height-1,-1,-1):
                    if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "rlbt":
            for r in range(height-1, -1, -1):
                for c in range(width-1, -1, -1):
                    if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "lrbt":
            for r in range(height - 1, -1, -1):
                for c in range(width):
                    if len(bits) < bits_needed:
                        if red:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if green:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(bits) == bits_needed:
                            break
                        if blue:
                            for b in range(int(depth)):  # Extract LSBs interleaved
                                bits.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
    bits = "".join(bits)
    bits = bits[64:]
    print("Number of bits: ", len(bits)+64)

    image = np.zeros((int(h), int(w), 3), dtype=np.uint8)
    bits_array = np.array([int(bits[i:i+8], 2) for i in range(0, len(bits), 8)], dtype=np.uint8)

    # Fill the image based on color order
    if color_order == "rgb":
        for r in range(int(h)):
            for c in range(int(w)):
                if len(bits_array) >= 3:
                    image[r, c, 0] = bits_array[0]  # Red
                    image[r, c, 1] = bits_array[1]  # Green
                    image[r, c, 2] = bits_array[2]  # Blue
                    bits_array = bits_array[3:]  # Remove used bits
                else:
                    break

    elif color_order == "bgr":
        for r in range(int(h)):
            for c in range(int(w)):
                if len(bits_array) >= 3:
                    image[r, c, 2] = bits_array[0]  # Blue
                    image[r, c, 1] = bits_array[1]  # Green
                    image[r, c, 0] = bits_array[2]  # Red
                    bits_array = bits_array[3:]  # Remove used bits
                else:
                    break
    

    imageio.imwrite(f"{folder}/{i.partition("/")[-1].partition(".")[0]}_{orient}_{color_ord}_{h}_{w}_{start_bit}_{depth}_{rd}_{gr}_{bl}.png", image)

def reverse_bits(n):
    reversed = 0
    for i in range(8):  # 8 bits
        reversed = (reversed << 1) | (n & 1)  # Shift reversed left, add LSB of n
        n >>= 1  # Shift n right
    return reversed

def flip_image(image, folder):
    img = imageio.imread(image)
    height, width, channels = img.shape

    for r in range(height):
        for c in range(width):
            img[r,c,0] = reverse_bits(img[r,c,0])
            img[r,c,1] = reverse_bits(img[r,c,1])
            img[r,c,2] = reverse_bits(img[r,c,2])
    imageio.imwrite(f"{folder}/{image.partition("/")[-1].partition(".")[0]}_reversed.png", img)

    
if __name__ == "__main__":
    find_img(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11])
