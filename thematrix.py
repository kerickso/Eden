#!/usr/bin/env python3

import sys
import math
import getopt
import tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH, HEIGHT = 800, 600
# WIDTH, HEIGHT = 1920, 1080

def width(bbox):
    return bbox[2] - bbox[0]

def height(bbox):
    return bbox[3] - bbox[1]

def shift(bbox, x, y):
    bbox[0] += x
    bbox[1] += y
    bbox[2] += x
    bbox[3] += y

def hackertext(text, font="/usr/share/fonts/TTF/DroidSansMono.ttf"):
    font = ImageFont.truetype(font, 80)
    boxes, size  = {}, (0, 0)

    y = 0
    # Map every line in the input text to a bounding box
    for line in text.split('\n'):
        boxes[line] = list(font.getmask(line).getbbox())
        shift(boxes[line], 0, y)
        y += 6 * height(boxes[line]) // 5
        size = max(size[0], boxes[line][2]), boxes[line][3]

    # Calculate a scale to size up the image
    k = math.ceil(max(size[0] / WIDTH, size[1] / HEIGHT))
    # Create a blank image with a black background to draw on
    image = Image.new('RGB', (k * WIDTH, k * HEIGHT), 0x000000)
    draw = ImageDraw.Draw(image)

    # Draw every line of text,
    for line, bbox in boxes.items():
        # Move the bounding box relative to the center of the image
        shift(bbox, (image.width - width(bbox)) // 2,
              (image.height - height(bbox) - size[1]) // 2)
        # Draw the text in green on the image and resize it to WIDTHxHEIGHT
        draw.text((bbox[0], bbox[1]), line, (0, 255, 0), font=font)

    image = image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    return image

def black_area(img):
    area = 0

    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) == (0, 0, 0):
                area += 1

    return area

def main():
    if (len(sys.argv) > 1):
        opts, args = getopt.getopt(sys.argv[1:], 'o:ih')
        opts = dict(opts)

        if '-h' in opts:
            print("""
Convert text to an image of green text on a black background

Usage:
    {} [OPTIONS] [INPUT TEXT]

Options:
    -o file : write output to the given file, uses tempfile by default
    -i      : read from stdin instead of command line arguments
    -h      : print this help and exit""".format(sys.argv[0])
            )

            exit()

        if '-i' in opts:
            text = []
            for line in sys.stdin.readlines():
                text.append('<{}>'.format(line.strip()))
            text = '\n'.join(text)

        else:
            text = '<{}>'.format(' '.join(args))

        outfile = opts.get('-o', tempfile.mktemp('.png', 'img_'))
        image = hackertext(text)

        # Blur relative to the percent of nonblack pixels
        nb = 1 - black_area(image) / (image.width * image.height)
        blur = math.ceil((nb ** 0.4) * 6)
        image = image.filter(ImageFilter.GaussianBlur(blur))
        print(nb ** 0.25, blur, file=sys.stderr)

        # Draw horizontal scanning lines over text
        draw = ImageDraw.Draw(image)
        for y in range(0, image.height, image.height // 40):
            draw.line([-1, y, image.width, y + 8], fill=0x2000, width=1)

        image.save(outfile)
        print(outfile)

if __name__ == '__main__':
    main()
