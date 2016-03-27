#!/usr/bin/env python3

import sys
import math
from PIL import Image, ImageDraw, ImageFont


def width(bbox):
    return bbox[2] - bbox[0]

def height(bbox):
    return bbox[3] - bbox[1]

def shift(bbox, x, y):
    bbox[0] += x
    bbox[1] += y
    bbox[2] += x
    bbox[3] += y

def hackertext(text, output="output.png"):
    font = ImageFont.truetype("/usr/share/fonts/TTF/DroidSansMono.ttf", 92)
    bbox = list(font.getmask(text).getbbox())

    # Calculate a scaled up size for the image
    k = max(math.ceil(width(bbox) / 800),
            math.ceil(height(bbox) / 600))
    w = 800 * k
    h = 600 * k

    # Create a black background image
    image = Image.new('RGB', (w, h), 0x000000)
    draw = ImageDraw.Draw(image)

    # Move the bounding box to the center of the image
    shift(bbox, w // 2 - width(bbox) // 2, h // 2 - height(bbox) // 2)

    # Draw the text in green on the image and resize it to 800x600
    draw.rectangle(bbox, outline=0xff)
    draw.text((bbox[0], bbox[1]), text, (0, 120, 0), font=font)
    image = image.resize((800, 600), Image.ANTIALIAS)
    image.save(output)

def main():
    if (len(sys.argv) > 1):
        hackertext('<{}>'.format(' '.join(sys.argv[1:])))

if __name__ == '__main__':
    main()
