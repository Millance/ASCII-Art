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
    parser.add_argument('--width', type=int, default=600, help='Number of output\'s width')
    parser.add_argument('--height', type=int, default=400, help='Number of output\'s height')
    parser.add_argument('--channel', type=int, default=3)  # 3:color, 1:gray
    parser.add_argument('--show', type=str, default='show')  # show, save
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    # 判断args.input是否为文件路径
    if os.path.isfile(args.input):
        # Read an image
        img = cv2.imread(args.input, 1)
        img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    else:
        # Generate a random image
        img = utils.textImg_generator(args.width, args.height, args.channel)

    stat_time = time.time()
    ascii_art = converter.image_to_ascii(img, width=args.width)
    print(int((time.time() - stat_time) * 1000), 'ms')
    if args.show == 'show':
        show_img = np.hstack((img, ascii_art))
        cv2.imshow('random_image.jpg', show_img)
        cv2.waitKey(0)
    else:
        cv2.imwrite(args.output + 'random_image_{}.jpg'.format(int(stat_time)), ascii_art)


if __name__ == '__main__':
    main()
