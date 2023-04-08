import time
import numpy as np
import Tools.converter as converter
import cv2
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Convert an image to ASCII art')
    parser.add_argument('--width', type=int, default=600, help='Number of output\'s width')
    parser.add_argument('--height', type=int, default=400, help='Number of output\'s height')
    parser.add_argument('--channel', type=int, default=3)  # 3:color, 1:gray
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    # 打开默认摄像头
    cap = cv2.VideoCapture(0)
    # 判断摄像头是否打开
    if not cap.isOpened():
        print('Cannot open camera!')
        exit()

    # 初始化帧数和计时器
    frame_count = 0
    frame_time = time.time()
    fps = 0

    while True:
        # 逐帧读取视频流
        ret, frame = cap.read()
        if args.channel == 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = np.expand_dims(frame, axis=-1)

        # 在窗口中显示视频流
        img = converter.image_to_ascii(frame, args.width)
        # 计算时间间隔
        current_time = time.time()
        elapsed_time = current_time - frame_time
        # 帧数加1
        frame_count += 1
        # 如果时间间隔大于等于1秒，则更新帧速率显示
        if elapsed_time >= 1.0:
            fps = frame_count / elapsed_time
            # 重置帧数和计时器
            frame_count = 0
            frame_time = time.time()
        # 在图形中显示帧速率
        cv2.putText(img, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

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
