from manim import config


def pixels_to_units(pixel_value, pixel_width, pixel_height, frame_width, frame_height, dimension='width'):
    """
    Convert pixel values to Manim units

    :param pixel_value: Number of pixels
    :param dimension: 'width' or 'height'
    :return: Equivalent value in Manim units
    """
    if dimension == 'width':
        return (pixel_value / pixel_width) * frame_width
    elif dimension == 'height':
        return (pixel_value / pixel_height) * frame_height
    else:
        raise ValueError("Dimension must be 'width' or 'height'")

if __name__ == "__main__":
    width = pixels_to_units(1920,config.pixel_width,config.pixel_height,config.frame_width,config.frame_height, dimension='width')
    height = pixels_to_units(1080,config.pixel_width,config.pixel_height,config.frame_width,config.frame_height, dimension='height')
    print(width)
    print(height)