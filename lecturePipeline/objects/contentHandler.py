import manim
from manim import *

from lecturePipeline.objects.sectionTitleMaker import sectionTitleMaker
from lecturePipeline.typography.text import textHandler
from lecturePipeline.utils.percent_to_units import percent_to_units


def contentHandler(text: str = "Characteristics of Numerical Relativity Initial Values",
                   duration: float = 3.0,
                   config= manim.config,
                   alignment=LEFT,
                   placement="title-on-left"):
    if placement == "title-only":
        return None
    elif placement == "title-on-left":
        return textHandler(text, "fluid.heading-04-mx", config, 200, RIGHT, alignment)


class TestScene(Scene):
    def construct(self):


        titleText = "A Simple Title"
        contentText = r"Hello, this is practically a very large piece of text with mathematics such as $\int$."
        placement = "title-on-left"
        lines = contentHandler(text = contentText, placement = placement)
        for i, line in enumerate(lines):
            self.play(FadeIn(line), run_time=0.25)
        self.wait(3)

        titleLines = sectionTitleMaker(placement=placement, text=titleText)

        for i, line in enumerate(titleLines):
            self.play(FadeIn(line), run_time=0.25)
        self.wait(3)
