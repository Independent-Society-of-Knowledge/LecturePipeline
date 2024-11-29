import manim
from PIL.ImageOps import cover
from manim import *

from lecturePipeline.typography.fonts.typography import typography, split_text_to_char_number
from lecturePipeline.typography.text import textHandler
from lecturePipeline.utils.percent_to_units import percent_to_units
from lecturePipeline.utils.pixel_to_units import pixels_to_units


def sectionTitleMaker(
        text: str = "Characteristics of Numerical Relativity Initial Values",
        max_char: int = 10,
        loose_maximize: bool = False,
        config= manim.config,
        type: str = "tokens.heading-04",
        alignment=RIGHT,
        placement="title-and-content-left"
):
    if "content" in placement:
        lines = split_text_to_char_number(text, 20, loose_maximize)
    else:
        lines = split_text_to_char_number(text, max_char, loose_maximize)
    coefs = pixels_to_units(config)
    typo = typography(type)
    font_size = typo['size']
    if placement == "title-only":
        return [Text(line, font_size=font_size, font="IBM Plex Mono").move_to(ORIGIN + i * 0.22 * DOWN,
                                                                              aligned_edge=alignment) for
                i, line in enumerate(lines)]
    elif placement == "title-on-left":
        return [
            Text(line, font_size=font_size, font="IBM Plex Mono").move_to(ORIGIN + i * 0.22 * DOWN, aligned_edge=RIGHT)
            for
            i, line in enumerate(lines)]
    elif placement == "title-on-right":
        return [
            Text(line, font_size=font_size, font="IBM Plex Mono").move_to(ORIGIN + i * 0.22 * DOWN, aligned_edge=LEFT)
            for
            i, line in enumerate(lines)]
    elif placement == "title-and-content-right":
        return [Text(line, font_size=font_size, font="IBM Plex Mono").move_to(
            percent_to_units(10, config, dimension="width") * RIGHT + i * 0.22 * DOWN + 3.5 * UP, aligned_edge=LEFT) for
            i, line in enumerate(lines)]
    elif placement == "title-and-content-left":
        return [Text(line, font_size=font_size, font="IBM Plex Mono").move_to(
            percent_to_units(45, config, dimension="width") * LEFT + i * 0.22 * DOWN + 3.5 * UP, aligned_edge=LEFT) for
            i, line in enumerate(lines)]



class testScene(Scene):
    def construct(self):
        lines = sectionTitleMaker()
        # self.add(Rectangle(width=16, height=9, color=BLUE, fill_color=BLUE, fill_opacity=0.5))
        self.add(ImageMobject("/home/kid-a/Pictures/pawel-czerwinski-PPo9tjzjcPg-unsplash.jpg"))
        self.add(Rectangle(width=percent_to_units(50, config, dimension="width"), height=9, fill_color=BLACK,
                           fill_opacity=1.0, stroke_width=0).move_to(ORIGIN, aligned_edge=RIGHT))
        for i, line in enumerate(lines):
            self.play(FadeIn(line), run_time=0.25)
        self.wait(3)
