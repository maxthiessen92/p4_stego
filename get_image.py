import numpy as np
import imageio
import sys

# Gets the header when its stored in the first 64 LSB.
def getFrequentHeader(imageName):
    img = imageio.imread(imageName)
    height, width, _ = img.shape

    bits = []
    count = 0
    for r in range(height):
        for c in range(width):
            for channel in range(3):
                bits.append(str(img[r, c, channel] & 1))
                count += 1
                if count == 64:
                    break
            if count == 64:
                break
        if count == 64:
            break

    bitsStr = ''.join(bits)  # Joins the bits
    
    hiddenHeight, hiddenWidth = getHeaderInfo(bitsStr)

    print(f"Height: {hiddenHeight}")
    print(f"Width: {hiddenWidth}")

# Gets the hidden image if stored right after the first 64 LSB and we have the header.
def getFrequentImage(imageName, hiddenHeight, hiddenWidth):
    # Reads the image
    img = imageio.imread(imageName)
    height, width, _ = img.shape

    totalBitsNeeded = hiddenHeight * hiddenWidth * 3 * 8
    totalBitsToRead = 64 + totalBitsNeeded

    # Collects the bits
    bits = []
    count = 0

    for r in range(height):
        for c in range(width):
            for channel in range(3):  # Gets only the three channels rgb
                bits.append(str(img[r, c, channel] & 1))  # Extracts LSB for each channel and appends to bits
                count += 1
                if count >= totalBitsToRead:
                    break
            if count >= totalBitsToRead:
                break
        if count >= totalBitsToRead:
            break

    # Removes header bits
    hiddenBits = bits[64:]

    numPixels = hiddenHeight * hiddenWidth
    pixelData = []
    i = 0

    # Builds hidden image from the bits for each channel
    for p in range(numPixels):
        pixel = []
        for _ in range(3):
            channelBits = ''.join(hiddenBits[i:i+8])
            i += 8
            value = int(channelBits, 2)
            pixel.append(value)
        pixelData.append(pixel)

    # Converts to image array and saves.
    hiddenImgArray = np.array(pixelData, dtype=np.uint8)
    hiddenImgArray = hiddenImgArray.reshape((hiddenHeight, hiddenWidth, 3))

    imageio.imwrite("hidden_image.png", hiddenImgArray)

# Builds the image created from the most LSB from a starting pixel to an ending pixel, with the specified dimensions.
def searchImageInRange(imageName, pixelStart, pixelEnd, hiddenHeight, hiddenWidth):
    # Reads the image
    img = imageio.imread(imageName)
    height, width, _ = img.shape

    numPixels = hiddenHeight * hiddenWidth
    totalBitsNeeded = numPixels * 3 * 8

    bits = []
    pixelCount = 0
    for r in range(height):
        for c in range(width):
            if pixelCount >= pixelEnd:
                break
            if pixelStart <= pixelCount < pixelEnd:
                for channel in range(3):
                    bits.append(str(img[r, c, channel] & 1))
            pixelCount += 1
        if pixelCount >= pixelEnd:
            break

    bits = bits[:totalBitsNeeded]

    bitsPerPixel = 3 * 8
    pixelData = []
    i = 0
    for _ in range(numPixels):
        pixel = []
        for channel in range(3):
            channelBits = ''.join(bits[i:i+8])
            i += 8
            channelValue = int(channelBits, 2)
            pixel.append(channelValue)
        pixelData.append(pixel)

    hiddenImgArray = np.array(pixelData, dtype=np.uint8)
    hiddenImgArray = hiddenImgArray.reshape((hiddenHeight, hiddenWidth, 3))


    imageio.imwrite("hiddenRange.png", hiddenImgArray)

# Gets all the LSB from the image.
def getAllLSBS(img):
    height, width, _ = img.shape

    bits = []
    for r in range(height):
        for c in range(width):
            for channel in range(3):
                bits.append(str(img[r, c, channel] & 1))
    return ''.join(bits)

# Interprets 64 bits as a image header. 
def getHeaderInfo(bits):
    heightBits = bits[:32]
    widthBits = bits[32:]
    hiddenHeight = int(heightBits, 2)
    hiddenWidth = int(widthBits, 2)
    return hiddenHeight, hiddenWidth

# Finds potential headers in the image by brute forcing.
def findPotentialHeader(imageName):
    img = imageio.imread(imageName)
    height, width, _ = img.shape

    bits = getAllLSBS(img)
    totalBits = len(bits)

    maxDimension = max(height, width) * 2 # Maximum dimension a hidden image can be

    potentialHeaders = []

    # Goes through the bits, analyzing whether it is a possible header or not.
    for i in range(0, totalBits - 64):
        bitsSegment = bits[i:i+64] # Gets first possible bit header combination
        hiddenHeight, hiddenWidth = getHeaderInfo(bitsSegment)

        # Checks whether the interpretation of bits can be a header.
        if (0 < hiddenHeight <= maxDimension) and (0 < hiddenWidth <= maxDimension): # Verifies that the value stored is not higher than the maximum dimension.
            totalBitsNeeded = hiddenHeight * hiddenWidth * 3 * 8 # Total number of bits to store hidden image.
            totalBitsAvailable = totalBits - (i + 64) # Calculates number of bits remaining after header.
            if totalBitsNeeded <= totalBitsAvailable: # If lower, it adds it to the possibility if its a header.
                potentialHeaders.append((i, hiddenHeight, hiddenWidth))

    if not potentialHeaders:
        print("No headers found.")
        return

    for i, (startingBit, possibleHeight, possibleWidth) in enumerate(potentialHeaders):
        print(f"Bit: {startingBit}, Height: {possibleHeight}, Width: {possibleWidth}" )

# Builds a hidden image after specifying where the starting bit and dimensions.
def getHiddenImage(imageName, headerStart, height, width):
    img = imageio.imread(imageName)
    bitstream = getAllLSBS(img)
    imageStart = headerStart + 64 

    totalBitsNeeded = height * width * 3 * 8

    bits = bitstream[imageStart:imageStart + totalBitsNeeded] # Gets the bits of hidden image.

    numPixels = height * width
    pixelData = []
    i = 0

    # Builds hidden image from the bits for each channel
    for p in range(numPixels):
        pixel = []
        for channel in range(3):
            channelBits = bits[i:i+8]
            i += 8
            channelValue = int(channelBits, 2)
            pixel.append(channelValue)
        pixelData.append(pixel)

    # Converts to image array and saves.
    hiddenImgArray = np.array(pixelData, dtype=np.uint8)
    hiddenImgArray = hiddenImgArray.reshape((height, width, 3))

    imageio.imwrite("potentialImage.png", hiddenImgArray)

if __name__ == "__main__": 
    
    if sys.argv[1] == "-getFrequentHeader":
        getFrequentHeader(sys.argv[2])
    
    if sys.argv[1] == "-getFrequentImage":
        getFrequentImage(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    
    if sys.argv[1] == "-searchImageInRange":
        searchImageInRange(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
    
    if sys.argv[1] == "-findPotentialHeader":
        findPotentialHeader(sys.argv[2])

    if sys.argv[1] == "-getHiddenImage":
        getHiddenImage(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))