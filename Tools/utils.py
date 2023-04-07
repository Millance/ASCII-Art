import numpy as np
import cv2


def textImg_generator(width=800, height=600, colors=3, shape_num=100):
    assert colors == 3 or colors == 1, 'Only support 3 or 1 colors'
    # 定义图像的大小和颜色数
    mean_shape_area = max(10, width * height // shape_num)
    # 创建一个黑色背景
    img = np.zeros((height, width, colors), np.uint8)

    # 循环生成随机形状和颜色
    for i in range(shape_num):
        # 随机选择形状（1 = 矩形，2 = 圆形，3 = 三角形，4 = 梯形，5 = 菱形）
        shape = np.random.randint(1, 6)
        # 随机选择颜色
        color = tuple(np.random.randint(0, 256) for _ in range(colors))
        # 随机生成形状面积
        area = np.random.randint(mean_shape_area // 2, mean_shape_area * 2)
        # 随机生成一个参考点 左上点坐标或中心点坐标
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        # 根据形状生成随机位置和大小
        if shape == 1:  # 矩形
            # 随机生成宽和高
            w = int(np.sqrt(area * width / height))
            h = int(area / w)
            # 绘制矩形
            cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
        elif shape == 2:  # 圆形
            # 随机生成圆半径
            r = int(np.sqrt(area / np.pi))
            # 绘制圆形
            cv2.circle(img, (x, y), r, color, -1)
        elif shape == 3:  # 三角形
            # 计算三角形边长
            edge_length = np.sqrt(4 * area / np.sqrt(3))
            # 生成随机角度
            angle = np.random.rand() * 2 * np.pi
            # 计算三个点的坐标
            x1, y1 = x + edge_length * np.cos(angle), y + edge_length * np.sin(angle)
            x2, y2 = x + edge_length * np.cos(angle + 2 / 3 * np.pi), y + edge_length * np.sin(angle + 2 / 3 * np.pi)
            x3, y3 = x + edge_length * np.cos(angle - 2 / 3 * np.pi), y + edge_length * np.sin(angle - 2 / 3 * np.pi)
            pts = np.array([[x1, y1], [x2, y2], [x3, y3]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(img, [pts], color)
        elif shape == 4:  # 梯形
            # 计算梯形的大小
            mean_shape_width = int(np.sqrt(area * 4 / 3))
            max_shape_width = int(mean_shape_width * 1.5)
            min_shape_width = int(mean_shape_width * 0.5)
            shape_width = np.random.randint(min_shape_width, max_shape_width)
            # 计算梯形的高度
            mean_shape_height = int(area / mean_shape_width)
            max_shape_height = int(mean_shape_height * 1.5)
            min_shape_height = int(mean_shape_height * 0.5)
            shape_height = np.random.randint(min_shape_height, max_shape_height)
            # 随机选择梯形的右上角坐标
            x1 = x + shape_width
            y1 = y
            # 随机选择梯形的左下角坐标
            x2 = x - np.random.randint(0, max(shape_width - min_shape_width, 1))
            y2 = y + shape_height
            # 随机选择梯形的右下角坐标
            x3 = x1 - np.random.randint(0, max(shape_width - min_shape_width, 1))
            y3 = y2
            # 构建梯形的坐标数组
            pts = np.array([[x, y], [x1, y1], [x3, y3], [x2, y2]], np.int32)
            # 绘制梯形
            cv2.fillPoly(img, [pts], color)
        elif shape == 5:  # 菱形
            # 生成随机菱形的顶点坐标
            half_l = int(np.sqrt(mean_shape_area) / 2)
            pts = np.array([[x - half_l, y], [x, y - half_l], [x + half_l, y], [x, y + half_l]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(img, [pts], color)
    return img
