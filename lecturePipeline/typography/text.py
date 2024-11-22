from manim import *
import textwrap
import re

from lecturePipeline.design.colors import getColor
from lecturePipeline.typography.fonts.typography import typography
from lecturePipeline.utils.pixel_to_units import pixels_to_units


def singleLineTex(
        input: str,
        type: str,
        config,
        max_width
):
    coefs = pixels_to_units(config)
    typo = typography(type)
    return Tex(input).scale_to_fit_height(typo['size'] / coefs[1])

def multiLineTex(
        input: list[str],
        type: str,
        config,
        max_width
):
    coefs = pixels_to_units(config)
    typo = typography(type)
    return [Tex(i).scale_to_fit_height(typo['size'] / coefs[1]) for i in input]
