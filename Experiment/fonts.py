import cv2
import numpy as np

# 获取OpenCV支持的所有字体类型
font_types = [x for x in dir(cv2) if x.startswith('FONT_')]

# 创建一个黑色的画布
canvas = 255 * np.ones((500, 1200, 3), dtype=np.uint8)

# 设置字体样式和大小
font_scale = 1
thickness = 2

# 遍历所有字体类型并在画布上绘制文本
for i, font_type in enumerate(font_types):
    font_face = getattr(cv2, font_type)
    text = font_type.replace('FONT_', '')
    y = (i + 1) * 40
    cv2.putText(canvas, text, (50, y), font_face, font_scale, (0, 0, 0), thickness)
    cv2.putText(canvas, text, (600, y), font_face, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)
    print(f"{font_type}: {font_face}")

# 显示画布
cv2.imshow('Fonts', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
