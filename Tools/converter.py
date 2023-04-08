import numpy as np
import cv2

# Define the grayscale values for ASCII characters
# char_str = '@%#*+=-:. '
char_str = 'M@WH%N8FbVpev<!}^:`. '
ascii_chars = np.asarray([char for char in char_str]).reshape(1, -1)
ascii_chars_count = ascii_chars.shape[1]  # Number of ASCII characters
font_scale = 0.3
thickness = 1
margin = 1


def image_to_ascii(image, width=100):
    # Calculate the new width and height of the image
    orig_height, orig_width, channels = image.shape
    aspect_ratio = orig_height / float(orig_width)
    new_height = int(width * aspect_ratio)
    new_width = width

    # Calculate the maximum size of each ASCII character
    size = np.asarray(
        [cv2.getTextSize(ascii_chars[0][i], cv2.FONT_HERSHEY_TRIPLEX, font_scale, thickness)[0] for i in
         range(ascii_chars_count)])
    # Maximum width and height of an ASCII character
    char_width = np.max(size[:, 0]) + margin
    char_height = np.max(size[:, 1]) + margin
    preview_width = new_width
    preview_height = new_height

    # Resize the image
    img_width = int(new_width / char_width) + 1
    img_height = int(new_height / char_height) + 1
    new_image = cv2.resize(image, (img_width, img_height))

    if channels == 1:
        new_image = np.expand_dims(new_image, axis=-1)
    ascii_matrix_list = []
    # Map pixel values to ASCII characters
    for i in range(channels):
        ascii_matrix = np.take_along_axis(ascii_chars,
                                          (new_image[:, :, i] / 255.0 * (ascii_chars_count - 1)).astype(int), axis=-1)
        ascii_matrix_list.append(ascii_matrix.astype(str))

    preview_image_list = []
    # Convert each ASCII matrix to a color image
    for i in range(channels):
        preview_image = np.ones((preview_height, preview_width), dtype=np.uint8) * 255
        for y in range(img_height):
            for x in range(img_width):
                char = ascii_matrix_list[i][y][x]
                left = x * char_width
                top = (y + 1) * char_height
                cv2.putText(preview_image, char, (left, top), cv2.FONT_HERSHEY_TRIPLEX, font_scale, 0, thickness,
                            cv2.LINE_AA)
        preview_image_list.append(preview_image)

    new_preview = np.stack([preview_image_list[i] for i in range(channels)], axis=2)
    return new_preview
