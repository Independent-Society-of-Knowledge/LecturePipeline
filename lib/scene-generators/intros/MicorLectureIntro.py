from manim import *

userTitle = input("What is the title of the video?")
title = Text(userTitle, font_size=32, fill_opacity=1, color=WHITE)
title.to_edge(LEFT)

class myScene(Scene):
    global title
    def construct(self):
       self.add(title)
       self.play(Create(title))
 
    
