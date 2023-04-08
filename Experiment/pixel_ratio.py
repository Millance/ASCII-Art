import cv2
import numpy as np
import string

# 要处理的字符集
char_set = string.printable[:-5]

# 读取字体
font = cv2.FONT_HERSHEY_TRIPLEX
# 定义字体大小和厚度
font_scale = 1
thickness = 2
margin = 10

# 计算所有字符的长宽，并求得最大值
font_size = np.asarray([cv2.getTextSize(char, font, font_scale, thickness)[0] for char in char_set])
max_width = np.max(font_size[:, 0])
max_height = np.max(font_size[:, 1])

# 使用max_width和max_height中的最大值来初始化画布
count = len(char_set)
char_space_w = max_width + margin
char_space_h = max_height + margin
canvas_width = int(char_space_w * 10)
canvas_height = int(char_space_h * (count / 10 + 1))
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# 绘制字符并计算像素和空间比率
ratios = []
for i, char in enumerate(char_set):
    # 在画布上绘制字符
    (w, h), _ = cv2.getTextSize(char, font, font_scale, thickness)
    x = int(i % 10 * char_space_w) + int((char_space_w - w) / 2)
    y = (int(i // 10) + 1) * char_space_h
    cv2.putText(canvas, char, (x, y), font, font_scale, (255, 255, 255), thickness)

    # 计算像素和空间比率
    ratio = cv2.countNonZero(cv2.cvtColor(canvas[y - max_height:y, x:x + max_width], cv2.COLOR_BGR2GRAY)) / (
            max_height * max_width)
    ratios.append((char, ratio))

# 将 ratios 中的比例按从大到小排序
ratios.sort(key=lambda x: x[1], reverse=True)

# for char, ratio in ratios:
#     print(f"{char}: {ratio}")
#
# # 输出字符
# temp_ratio = 0
# for char, ratio in ratios:
#     if ratio != temp_ratio:
#         print(char, end='')
#         temp_ratio = ratio

# 每个比例范围的步长为 2%
step = 0.02
# 当前比例范围的最小值，初始为 0
cur_min_ratio = 0
reverse_str = ""
# 遍历比例范围，输出每个范围的字符
while cur_min_ratio <= 1:
    # 计算当前比例范围的最大值
    cur_max_ratio = cur_min_ratio + step
    # 找到在当前比例范围内的所有字符
    chars_in_range = [char for char, ratio in ratios if cur_min_ratio <= ratio < cur_max_ratio]
    # 如果当前范围内有字符，则从中随机选择一个输出
    if chars_in_range:
        output_char = np.random.choice(chars_in_range)
        print(output_char, end='')
        reverse_str = output_char + reverse_str
    # 更新比例范围的最小值
    cur_min_ratio = cur_max_ratio
print()
print(reverse_str)

# cv2.imshow('Fonts', canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
