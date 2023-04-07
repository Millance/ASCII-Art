import numpy as np
import cv2


def img_generator(width=800, height=600, colors=3, shape_num=100):
    assert colors == 3 or colors == 1, 'Only support 3 or 1 colors'
    # Define the size of the image and the number of shapes to generate
    mean_shape_area = max(10, width * height // shape_num)
    # Create a black background image
    img = np.zeros((height, width, colors), np.uint8)

    # Loop to generate random shapes and colors
    for i in range(shape_num):
        # Randomly select a shape (1 = rectangle, 2 = circle, 3 = triangle, 4 = trapezoid, 5 = diamond)
        shape = np.random.randint(1, 6)
        # Randomly select a color
        color = tuple(np.random.randint(0, 256) for _ in range(colors))
        # Randomly generate the area of the shape
        area = np.random.randint(mean_shape_area // 2, mean_shape_area * 2)
        # Randomly generate a reference point, either the upper left corner or the center point
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        # Generate random position and size according to the shape
        if shape == 1:  # Rectangle
            # Randomly generate width and height
            w = int(np.sqrt(area * width / height))
            h = int(area / w)
            # Draw the rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
        elif shape == 2:  # Circle
            # Randomly generate the radius of the circle
            r = int(np.sqrt(area / np.pi))
            # Draw the circle
            cv2.circle(img, (x, y), r, color, -1)
        elif shape == 3:  # Triangle
            # Calculate the length of the triangle's sides
            edge_length = np.sqrt(4 * area / np.sqrt(3))
            # Generate a random angle
            angle = np.random.rand() * 2 * np.pi
            # Calculate the coordinates of the three points
            x1, y1 = x + edge_length * np.cos(angle), y + edge_length * np.sin(angle)
            x2, y2 = x + edge_length * np.cos(angle + 2 / 3 * np.pi), y + edge_length * np.sin(angle + 2 / 3 * np.pi)
            x3, y3 = x + edge_length * np.cos(angle - 2 / 3 * np.pi), y + edge_length * np.sin(angle - 2 / 3 * np.pi)
            pts = np.array([[x1, y1], [x2, y2], [x3, y3]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(img, [pts], color)
        elif shape == 4:  # Trapezoid
            # Calculate the size of the trapezoid
            mean_shape_width = int(np.sqrt(area * 4 / 3))
            max_shape_width = int(mean_shape_width * 1.5)
            min_shape_width = int(mean_shape_width * 0.5)
            shape_width = np.random.randint(min_shape_width, max_shape_width)
            # Calculate the height of the trapezoid
            mean_shape_height = int(area / mean_shape_width)
            max_shape_height = int(mean_shape_height * 1.5)
            min_shape_height = int(mean_shape_height * 0.5)
            # Randomly select the height of the shape within the given range
            shape_height = np.random.randint(min_shape_height, max_shape_height)
            # Randomly select the coordinates of the upper-right corner of the trapezoid
            x1 = x + shape_width
            y1 = y
            # Randomly select the coordinates of the lower-left corner of the trapezoid
            x2 = x - np.random.randint(0, max(shape_width - min_shape_width, 1))
            y2 = y + shape_height
            # Randomly select the coordinates of the lower-right corner of the trapezoid
            x3 = x1 - np.random.randint(0, max(shape_width - min_shape_width, 1))
            y3 = y2
            # Construct an array of coordinates to create the trapezoid shape
            pts = np.array([[x, y], [x1, y1], [x3, y3], [x2, y2]], np.int32)
            # Draw the trapezoid shape
            cv2.fillPoly(img, [pts], color)
        elif shape == 5:  # diamond
            # Generate random vertex coordinates for the diamond
            half_l = int(np.sqrt(mean_shape_area) / 2)
            pts = np.array([[x - half_l, y], [x, y - half_l], [x + half_l, y], [x, y + half_l]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(img, [pts], color)
    return img
