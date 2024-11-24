from manim import *
from lecturePipeline.typography.fonts.typography import typography, calculate_text_width, split_text_to_width, \
    computeLineSpacing, calculate_scaling_factor
from lecturePipeline.utils.pixel_to_units import pixels_to_units


def textHandler(
        input: str,
        type: str,
        config,
        width: float = None,
        position = ORIGIN
):
    """Main entry point for text handling. Processes text and manages line breaks if needed."""
    coefs = pixels_to_units(config)
    typo = typography(type)
    font_size = typo['size']

    if width is None or calculate_text_width(input, font_size) < width:
        return [Tex(input, font_size= font_size)]

    else:
        lines = split_text_to_width(input, width, font_size)
        return lineHandler(lines, type, config, font_size, position)


def lineHandler(
        lines: list[str],
        type: str,
        config,
        font_size: float,
        position
):
    """Handles the spacing and arrangement of multiple lines."""
    coefs = pixels_to_units(config)
    typo = typography(type)
    linespacing = computeLineSpacing(fontSize=typo['size'], lineHeightMultiplier=typo['lh'],
                                     lineSpacingMultiplier=typo['ls'])
    # print(linespacing)
    # Create Tex objects for each line with consistent height scaling
    print(linespacing / coefs[1]**1.5)
    return [Tex(line, font_size = font_size ).move_to(DOWN * i * linespacing / (coefs[1]) + position, aligned_edge=LEFT) for
            i, line in enumerate(lines)]




class testScene(Scene):
    def construct(self):
        text = textHandler(
            input="This is a line that would be wrapped into multiline.",
            type="fluid.display-04-mx",
            config=config,
            width=100)

        # # Multiple lines with width constraint
        # lines = multiLineTex([
        #     "First long line that might wrap",
        #     "Second line that could also be too long"
        # ], "fluid.display-01-sm", config, width=100)
        for t in text:
            self.add(t)
            self.add(Line(LEFT, RIGHT))
        # self.add(lines)
