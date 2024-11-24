from manim import config


def pixels_to_units(config):
    """
    Convert pixel values to Manim units
    :param config: dictionary with manim configuration
    :return: Coefficients of the units
    """
    return [config.pixel_width / config.frame_width, config.pixel_height / config.frame_height]
