from manim import *


class Titlescene(Scene):
    def construct(self):
        def titlescene(title: str, subtitle: str, mode: int):
            self.camera.background_color = BLUE
            boundary = Rectangle(height=1, width=1,
                                fill_color=BLACK, stroke_color=BLACK,
                                fill_opacity=1)
            title_text = Text(title, font_size=60)
            subtitle_text = Text(subtitle, font_size=45)
            
            
            if mode ==1:
                boundary.scale([8, 4, 1]).to_edge(LEFT)
                title_text.align_to(boundary, UL).shift(0.1*DOWN, 0.2*RIGHT)
                subtitle_text.align_to(boundary, DL).shift(0.1*UP + 0.2*RIGHT)
                
            elif mode ==2:
                boundary.scale([5.5, 5, 1])
                title_text.align_to(boundary, UP).shift(0.2*DOWN)
                subtitle_text.align_to(boundary, DOWN).shift(0.2*UP)
                
            elif mode ==3:
                boundary.scale([9, 3.3, 1])
                title_text.align_to(boundary, LEFT).shift(0.2*RIGHT)
                subtitle_text.align_to(boundary, RIGHT).shift(0.2*LEFT)
                
            elif mode ==4:
                boundary.scale([7, 5, 1])
                boundary.to_corner(DR).shift(0.5*DOWN + 0.5*RIGHT)
                title_text.align_to(boundary, UL).shift(0.2*RIGHT + 0.2*DOWN)
                subtitle_text.align_to(boundary, DL).shift(0.2*RIGHT + 0.2*UP)
                
            elif mode ==5:
                boundary.scale([7, 8, 1])
                boundary.to_edge(RIGHT).shift(0.5*RIGHT)
                title_text.align_to(boundary, LEFT).shift(0.2*RIGHT)
                subtitle_text.next_to(title_text, DOWN, aligned_edge=LEFT)
                
            elif mode ==6:
                boundary.scale([7, 8, 1])
                boundary.to_edge(LEFT).shift(0.2*LEFT)
                title_text.align_to(boundary, LEFT).shift(RIGHT)
                subtitle_text.next_to(title_text, DOWN, aligned_edge=LEFT)
                
            elif mode ==7:
                boundary.scale([7, 8, 1])
                boundary.to_corner(UL).shift(0.5*LEFT + 0.5*UP)
                title_text.move_to(boundary.get_center())
                subtitle_text.next_to(title_text, DOWN, aligned_edge=LEFT)
                  
            self.add(boundary)
            self.play(Write(title_text))
            self.play(Write(subtitle_text))
            self.wait()
        

        titlescene("A", "B", 1)