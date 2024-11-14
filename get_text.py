
import numpy as np
import imageio
import sys

#returns a number value that represents a hidden header
#input the image source, the start bit, and the end bit of where you want to test the header location
def check_header(image, header_start, header_end, depth):
    # read in image
    img = imageio.imread(image)
    length = int(header_end)//int(depth)
    height, width, _ = img.shape
    print("Height:", height, "Width:", width)
    print("Max Characters:", height*width * (3*int(depth)) / 8)
    lsbs = (1 << int(depth)) - 1
    chars = []
    red = bool(int(sys.argv[6]))
    green = bool(int(sys.argv[7]))
    blue = bool(int(sys.argv[8]))
    orientation = sys.argv[9].lower()
    #get the lsb of channels and put it in a char array which will be length header_end
    if orientation == "lrtb":
        for r in range(height):
            for c in range(width):
                if len(chars) < length:
                    if red:
                        chars.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if green:
                        chars.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if blue:
                        chars.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
    elif orientation == "rltb":
        for r in range(height):
            for c in range(width-1, -1, -1):
                if len(chars) < length:
                    if red:
                        chars.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if green:
                        chars.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if blue:
                        chars.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
    elif orientation == "tblr":
        for c in range(height):
            for r in range(width):
                if len(chars) < length:
                    if red:
                        chars.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if green:
                        chars.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if blue:
                        chars.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
    elif orientation == "btlr":
        for c in range(height):
            for r in range(width -1, -1, -1):
                if len(chars) < length:
                    if red:
                        chars.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if green:
                        chars.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if blue:
                        chars.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
    elif orientation == "lrbt":
        for r in range(height-1, -1, -1):
            for c in range(width):
                if len(chars) < length:
                    if red:
                        chars.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if green:
                        chars.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if blue:
                        chars.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
    elif orientation == "rlbt":
        for r in range(height-1, -1, -1):
            for c in range(width-1, -1, -1):
                if len(chars) < length:
                    if red:
                        chars.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if green:
                        chars.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
                    if blue:
                        chars.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(chars) == length:
                        break
               
    #set the header to a string from the inputed header_start to the end of the char array
    header = "".join(chars[int(header_start)//int(depth):])

    #convert the binary string to decimal
    message_length = int(header, 2)
    print(header)
    print(message_length)
    #return the found number
    return message_length

# finds a string from an image
# inputs: image source, the bit number where you suspect the header ends, the suspected message length, 
# the suspected number of lsbs taken from each channel to hide the message
def find_message(image, header_end, message_length, depth):
    #load the image
    img = imageio.imread(image)
    length = int(header_end)
    print(f"header length: {length}")
    print(f"header value: {int(message_length)}")
    height, width, _ = img.shape
    print("Height:", height, "Width:", width)
    print("Max Characters:", height*width * (3*int(depth)) / 8)
    #create a mask to extract the lsbs
    lsbs = (1 << int(depth)) - 1
    print(lsbs)
    red = bool(int(sys.argv[6]))
    green = bool(int(sys.argv[7]))
    blue = bool(int(sys.argv[8]))
    orientation = sys.argv[9].lower()
    #will initially hold the bits of the header and the message
    message = []
    if orientation == "lrtb":
        for r in range(height):
            for c in range(width):
                #if the length of the message array is less than the target number of bits
                # add the lsbs of a channel to the message array then check again for the next channel
                if len(message) < ((int(message_length)*8)+length)/int(depth):
                    if red:
                        message.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if green:
                        message.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if blue:
                        message.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
    elif orientation == "rltb":
        for r in range(height):
            for c in range(width-1, -1, -1):
                #if the length of the message array is less than the target number of bits
                # add the lsbs of a channel to the message array then check again for the next channel
                if len(message) < ((int(message_length)*8)+length)/int(depth):
                    if red:
                        message.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if green:
                        message.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if blue:
                        message.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
    elif orientation == "tblr":
        for c in range(height):
            for r in range(width):
                #if the length of the message array is less than the target number of bits
                # add the lsbs of a channel to the message array then check again for the next channel
                if len(message) < ((int(message_length)*8)+length)/int(depth):
                    if red:
                        message.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if green:
                        message.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if blue:
                        message.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
    elif orientation == "btlr":
        for c in range(height):
            for r in range(width-1, -1, -1):
                #if the length of the message array is less than the target number of bits
                # add the lsbs of a channel to the message array then check again for the next channel
                if len(message) < ((int(message_length)*8)+length)/int(depth):
                    if red:
                        message.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if green:
                        message.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if blue:
                        message.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
    elif orientation == "lrbt":
        for r in range(height-1, -1, -1):
            for c in range(width):
                #if the length of the message array is less than the target number of bits
                # add the lsbs of a channel to the message array then check again for the next channel
                if len(message) < ((int(message_length)*8)+length)/int(depth):
                    if red:
                        message.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if green:
                        message.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if blue:
                        message.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
    elif orientation == "rlbt":
        for r in range(height-1, -1, -1):
            for c in range(width-1, -1, -1):
                #if the length of the message array is less than the target number of bits
                # add the lsbs of a channel to the message array then check again for the next channel
                if len(message) < ((int(message_length)*8)+length)/int(depth):
                    if red:
                        message.append(bin((img[r,c,0] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if green:
                        message.append(bin((img[r,c,1] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
                    if blue:
                        message.append(bin((img[r,c,2] & lsbs))[2:].zfill(int(depth)))
                    if len(message) == ((int(message_length)*8)+length)/int(depth):
                        break
    #get rid of the header bits from the message
    
    message = "".join(message)
    message = message[length:]
    

    final_message = []
    mask = 0b11111111
    
    #extract characters from the bit string character by character
    while len(message) > 0:
        final_message.append(chr(int(message[:8], 2) & mask))
        message = message[8:]

    final_message = "".join(final_message)
    text_file = open("Output.txt", "w")

    text_file.write(final_message)

    text_file.close()
    print(final_message)
    return(final_message)

if __name__ == "__main__":
    if sys.argv[1] == "-check_header":
        check_header(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    
    if sys.argv[1] == '-find_message':
        find_message(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])



    
