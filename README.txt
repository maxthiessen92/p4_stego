Required Libraries: numpy, imageio, sys
Required Python version: 3.10 or higher

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Five different files: 
get_text.py -> Contains functions that help find hidden text messages
get_image.py -> Contains functions that help find hidden images.
magnify_lsbs.py -> produces an image of magnified lsbs
find_img.py -> produces an hidden image from parameters.
master_script.py -> helps automate the process of finding things with these tools

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
get_text.py functionality:

to use get_header function:

python get_text.py -check_header <image_source_addr> <suspected_header_start_bit(0, 16, 32, etc.)> <suspected_header_end_bit depth(number of lsbs extracted)> <number of lsbs> <get from red channel (1 is yes, 0 is no)> <get from green channel (1 is yes, 0 is no)> <get from blue channel (1 is yes, 0 is no)> <orientation (lrtb, tblr, btlr, etc)>

to use find_message function:

python get_text.py -find_message <image_source_addr> <suspected_header_end_bit> <number_of_characters depth(number of lsbs)> <get red (1 or 0)> <get green (1 or 0)> <get blue <1 or 0> <orientation>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

get_image.py functionality:

- getFrequentHeader -> Gets the header when its stored in the first 64 LSB.
  To run: python get_image.py -getFrequentHeader <imagename.png>

- getFrequentImage -> Gets the hidden image if stored right after the first 64 LSB and we have the header.
  To run: python get_image.py -getFrequentImage <imagename.png> <height> <width>

- searchImageInRange -> Builds the image created from the LSB from a starting pixel to an ending pixel, with the specified dimensions.
  To run: python get_image.py -searchImageInRange <filename.png> <startingPixel> <endingPixel> <height> <width>

- findPotentialHeader -> Finds potential headers in the image by brute forcing
  To run: python get_image.py -findPotentialHeader <filename.png>

- getHiddenImage -> Builds a hidden image from LSB after specifying where the starting bit and dimensions.
  To run: python get_image.py -getHiddenImage <filename.png> <startingBit> <height> <width>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

magnify_lsbs.py functionality:

- to run: python magnify_lsbs.py <image_source_addr>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

find_img.py functionality:

- to run: python find_img.py <image_source_addr> <height> <width> <number of lsbs> <get red (1 or 0)> <get green (1 or 0)> <get blue (1 or 0)> <search orientation> <channel gathering order (rgb, bgr, etc.)>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

master_script.py functionality:

- to run: python master_script.py

Tools:

- check for headers in any possible orientation, saves console output as a text file
- create images of any bit in the channels you want to magnify
- generate hidden images through inputs
