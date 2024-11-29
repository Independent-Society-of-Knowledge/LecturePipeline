from manim import *


class EndScene(Scene):
    def construct(self):
        spacing_coefficient = 0.32
        center_margin = 0.15
        logo_1 = Tex("Independent", font_size=32).move_to(RIGHT + spacing_coefficient * UP, aligned_edge=RIGHT)
        logo_2 = Tex("Society of", font_size=32).move_to(RIGHT, aligned_edge=RIGHT)
        logo_3 = Tex("Knowledge", font_size=32).move_to(RIGHT + spacing_coefficient * DOWN, aligned_edge=RIGHT)

        self.play(FadeIn(logo_1), run_time=0.25)
        self.play(FadeIn(logo_2), run_time=0.25)
        self.play(FadeIn(logo_3), run_time=0.5)

        self.play(logo_1.animate.move_to(LEFT * center_margin + spacing_coefficient * UP, aligned_edge=RIGHT),
                  logo_2.animate.move_to(LEFT * center_margin, aligned_edge=RIGHT),
                  logo_3.animate.move_to(LEFT * center_margin + spacing_coefficient * DOWN, aligned_edge=RIGHT),
                  run_time=0.5)

        micro = Text("MICRO", font="IBM Plex Mono", font_size=24).move_to(RIGHT * center_margin + 0.1 * UP, aligned_edge=LEFT)
        lectures = Text("LECTURES", font="IBM Plex Mono", font_size=24).move_to(RIGHT * center_margin + 0.1 * DOWN, aligned_edge=LEFT)
        self.play(FadeIn(micro),FadeIn(lectures), run_time=0.5)

        self.wait(3)
