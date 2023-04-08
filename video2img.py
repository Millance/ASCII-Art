import time
import numpy as np
import Tools.converter as converter
import cv2
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Convert a video to ASCII art')
    parser.add_argument('--input', type=str, default='Data/data2.mp4', help='Path to input image')  # generate, path
    parser.add_argument('--width', type=int, default=600, help='Number of output\'s width')
    parser.add_argument('--height', type=int, default=400, help='Number of output\'s height')
    parser.add_argument('--channel', type=int, default=3)  # 3:color, 1:gray
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    # 打开默认摄像头
    cap = cv2.VideoCapture(args.input)
    # 判断摄像头是否打开
    if not cap.isOpened():
        print('Cannot open video!')
        exit()
    while True:
        # 逐帧读取视频流
        ret, frame = cap.read()
        if args.channel == 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = np.expand_dims(frame, axis=-1)

        # 在窗口中显示视频流
        img = converter.image_to_ascii(frame,  args.width)

        cv2.imshow('frame', img)
        # 按下q键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q') or cv2.waitKey(1) == 27:
            break

    # 释放摄像头资源
    cap.release()
    # 关闭所有窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
