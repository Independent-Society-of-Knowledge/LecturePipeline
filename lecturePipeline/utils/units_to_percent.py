from manim import *
def units_to_percent(units, frame_width, frame_height, dimensions="width"):
    if dimensions == "width":
        return units * 100 /frame_width
    elif dimensions == "height":
        return units * 100 /frame_height


if __name__ == "__main__":
    config.frame_width = 16
    config.frame_height = 9
    print(units_to_percent(16, config.frame_width, config.frame_height, dimensions="width"))
    print(units_to_percent(9, config.frame_width, config.frame_height, dimensions="height"))