from manim import *


def percent_to_units(percent_value, frame_width, frame_height, dimension='width'):
    """
    Convert pixel values to Manim units

    :param pixel_value: Number of pixels
    :param dimension: 'width' or 'height'
    :return: Equivalent value in Manim units
    """
    if dimension == 'width':
        return (percent_value * frame_width) / 100
    elif dimension == 'height':
        return (percent_value * frame_height) / 100
    else:
        raise ValueError("Dimension must be 'width' or 'height'")


if __name__ == "__main__":
    config.frame_height = 9
    config.frame_width = 16
    width = percent_to_units(100, config.frame_width, config.frame_height, dimension='width')
    height = percent_to_units(80, config.frame_width, config.frame_height, dimension='height')
    print(f"Width: {width}, with frame height: {config.frame_height}, frame width: {config.frame_width} ")
    print(f"Height: {height}, with frame height: {config.frame_height}, frame width: {config.frame_width} ")
