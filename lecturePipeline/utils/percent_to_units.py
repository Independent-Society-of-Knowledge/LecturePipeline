from manim import *


def percent_to_units(percent_value, config, dimension='width'):
    """
    Convert pixel values to Manim units

    :param pixel_value: Number of pixels
    :param dimension: 'width' or 'height'
    :return: Equivalent value in Manim units
    """
    if dimension == 'width':
        return (percent_value * config.frame_width) / 100
    elif dimension == 'height':
        return (percent_value * config.frame_height) / 100
    else:
        raise ValueError("Dimension must be 'width' or 'height'")

