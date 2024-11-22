
import numpy as np
import imageio
import sys

#returns a number value that represents a hidden header
#input the image source, the start bit, and the end bit of where you want to test the header location
def get_header(image, header_start, header_end, depth, rd, gr, bl, orient, start_bit):
    # read in image
    img = imageio.imread(image)
    length = int(header_end)
    height, width, _ = img.shape
    print("Height:", height, "Width:", width)
    print("Max Characters:", height*width * (3*int(depth)) / 8)
    lsbs = ((1 << int(depth)) - 1) << (int(start_bit)-1)
    chars = []
    red = bool(int(rd))
    green = bool(int(gr))
    blue = bool(int(bl))
    orientation = orient.lower()
    count = 0
    #get the lsb of channels and put it in a char array which will be length header_end
    match orientation:
        case "lrtb":
            for r in range(height):
                for c in range(width):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "rltb":
            for r in range(height):
                for c in range(width-1, -1, -1):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "tblr":
            for c in range(width):
                for r in range(height):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "tbrl":
            for c in range(width - 1, -1, -1):
                for r in range(height):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "btlr":
            for c in range(width):
                for r in range(height -1, -1, -1):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "btrl":
            for c in range(width-1, -1, -1):
                for r in range(height-1, -1, -1):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "lrbt":
            for r in range(height-1, -1, -1):
                for c in range(width):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
        case "rlbt":
            for r in range(height-1, -1, -1):
                for c in range(width-1, -1, -1):
                    if len(chars) < length:
                        if red:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if green:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(chars) == length:
                            break
                        if blue:
                            for b in range(int(depth)):
                                chars.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])

    #set the header to a string from the inputed header_start to the end of the char array
    header = "".join(chars)
    header = header[int(header_start):]
    print(f"Header length: {length}")
    if len(header) == 0:
        print("No characters")
        return (height, width), 0
    #convert the binary string to decimal
    message_length = int(header, 2)
    if message_length <= (height*width * (3*int(depth)) / 8) and message_length != 0:
        print("POTENTIAL MATCH")
        print(header)
        print(f"Message: {message_length}")
        return (height, width), message_length
    print(header)
    print(f"Message: {message_length}")
    return (height, width), 0
    #return the found number
    

# finds a string from an image
# inputs: image source, the bit number where you suspect the header ends, the suspected message length, 
# the suspected number of lsbs taken from each channel to hide the message
def find_message(image, header_end, message_length, depth, rd, gr, bl, orient, start_bit):
    #load the image
    img = imageio.imread(image)
    length = int(header_end)
    print(f"header length: {length}")
    print(f"header value: {int(message_length)}")
    height, width, _ = img.shape
    height = int(height)
    width = int(width)
    print("Height:", height, "Width:", width)
    print("Max Characters:", height*width * (3*int(depth)) / 8)
    #create a mask to extract the lsbs
    lsbs = ((1 << int(depth)) - 1) << (int(start_bit)-1)
    print(lsbs)
    red = bool(int(rd))
    green = bool(int(gr))
    blue = bool(int(bl))
    orientation = orient.lower()
    #will initially hold the bits of the header and the message
    message = []
    match orientation:
        case "lrtb":
            for r in range(int(height//2)):
                for c in range(width):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "rltb":
            for r in range(height//2):
                for c in range(width-1, -1, -1):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "tblr":
            for c in range(width//2):
                for r in range(height):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "tbrl":
            for c in range(width - 1, width//2, -1):
                for r in range(height):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "btlr":
            for c in range(width//2):
                for r in range(height-1, -1, -1):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "btrl":
            for c in range(width-1,width//2 , -1):
                for r in range(height-1, -1, -1):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "lrbt":
            for r in range(height-1, height//2, -1):
                for c in range(width):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                   if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        case "rlbt":
            for r in range(height-1, height//2, -1):
                for c in range(width-1, -1, -1):
                    #if the length of the message array is less than the target number of bits
                    # add the lsbs of a channel to the message array then check again for the next channel
                    if len(message) < ((int(message_length)*8)+length)/int(depth):
                       if red:
                        for b in range(int(depth)):
                                message.append(bin((img[r, c, 0] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if green:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 1] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
                        if blue:
                            for b in range(int(depth)):
                                message.append(bin((img[r, c, 2] & (1 << (b + int(start_bit) - 1))) >> (b + int(start_bit) - 1))[2:])
                        if len(message) == ((int(message_length)*8)+length)/int(depth):
                            print(f"{r}_{c}")
                            break
        
    #get rid of the header bits from the message
  
    message = "".join(message)
    message = message[length:]
    message_array = bytes(int(message[i:i+8], 2) for i in range(0, len(message), 8))



    

    #extract characters from the bit string character by character


    # print(message_array)
    # Decode the byte array into a string

    # final_message = ''.join(message_array)
    final_message = message_array.decode('utf-8', errors='replace')
    
    print(final_message)
    return final_message

if __name__ == "__main__":
    if sys.argv[1] == "-get_header":
        get_header(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])
    
    if sys.argv[1] == '-find_message':
        find_message(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])



    
