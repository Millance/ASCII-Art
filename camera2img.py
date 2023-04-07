import time
import Tools.converter as converter
import cv2

# 打开默认摄像头
cap = cv2.VideoCapture(0)
# 初始化帧数和计时器
frame_count = 0
frame_time = time.time()
fps = 0

while True:
    # 逐帧读取视频流
    ret, frame = cap.read()
    # 在窗口中显示视频流
    img = converter.image_to_ascii(frame, width=500)
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
