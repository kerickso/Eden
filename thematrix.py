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

def hackertext(text):
    font = ImageFont.truetype("/usr/share/fonts/TTF/DroidSansMono.ttf", 64)
    bbox = list(font.getmask(text).getbbox())

    # Calculate a scaled up size for the image
    k = max(math.ceil(width(bbox) / WIDTH),
            math.ceil(height(bbox) / HEIGHT))
    w = WIDTH * k
    h = HEIGHT * k
    # Create parameters based on how small the text will appear
    bright = k * 256 // (k + 1)
    blur = math.ceil(1.5 * k)
    print('>>>', k, file=sys.stderr) # debugging info

    # Create a black background image
    image = Image.new('RGB', (w, h), 0x000000)
    draw = ImageDraw.Draw(image)
    # Move the bounding box to the center of the image
    shift(bbox, (w - width(bbox)) // 2, (h - height(bbox)) // 2)
    # Draw the text in green on the image and resize it to WIDTHxHEIGHT
    draw.text((bbox[0], bbox[1]), text, (0, bright, 0), font=font)
    image = image.filter(ImageFilter.GaussianBlur(blur))
    image = image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    return image

def main():
    if (len(sys.argv) > 1):
        opts, args = getopt.getopt(sys.argv[1:], 'o:ih')
        opts = dict(opts)

        outfile = opts.get('-o', tempfile.mktemp('.png', 'img_'))
        text = input() if '-i' in opts else ' '.join(args)

        image = hackertext('<{}>'.format(text))
        image.save(outfile)

        print(outfile)

if __name__ == '__main__':
    main()
