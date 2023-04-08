import time
import numpy as np
import Tools.utils as utils
import Tools.converter as converter
import cv2
import os
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Convert an image to ASCII art')
    parser.add_argument('--input', type=str, default='generate', help='Path to input image')  # generate, path
    parser.add_argument('--output', type=str, default='Result/', help='Path to output text file')
    parser.add_argument('--converter', type=int, default=2, help='Convert method')  # 1:Typical, 2: Colorful characters
    parser.add_argument('--width', type=int, default=600, help='Number of output\'s width')
    parser.add_argument('--height', type=int, default=400, help='Number of output\'s height')
    parser.add_argument('--channel', type=int, default=3, help="Color or Gray")  # 3:color, 1:gray
    parser.add_argument('--font_scale', type=float, default=0.2, help='Font scale')
    parser.add_argument('--font_thickness', type=int, default=1, help='Font thickness')
    parser.add_argument('--show', type=str, default='show')  # show, save
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    # 判断args.input是否为文件路径
    if os.path.isfile(args.input):
        # Read an image
        img = cv2.imread(args.input, 1)
        img = cv2.resize(img, (args.width, args.height))
    else:
        # Generate a random image
        img = utils.img_generator(args.width, args.height, args.channel)

    stat_time = time.time()
    if args.converter == 1:
        ascii_art = converter.image_to_ascii(img, args.font_scale, args.font_thickness, args.width)
    else:
        ascii_art = converter.image_to_ascii_2(img, args.font_scale, args.font_thickness, args.width)
    print(int((time.time() - stat_time) * 1000), 'ms')
    if args.show == 'show':
        show_img = np.hstack((img, ascii_art))
        cv2.imshow('random_image.jpg', show_img)
        cv2.waitKey(0)
    else:
        show_img = np.hstack((img, ascii_art))
        cv2.imwrite(args.output + 'result_{}.jpg'.format(int(stat_time)), show_img)


if __name__ == '__main__':
    main()
