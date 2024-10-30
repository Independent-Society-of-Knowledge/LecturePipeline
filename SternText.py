from manim import *
class SternTexts(Scene):
    def construct(self):
        title = Text("Stern-Gerlach\nExperiment",
                     font_size=50,
                     fill_opacity=1,
                     color=WHITE)
        title.to_edge(LEFT)
        Definition = Text("Mircro Lecture Series",
                          font_size=20,
                          fill_opacity=1,
                          color=WHITE)
        Definition.to_edge(LEFT)
        Definition.shift(DOWN)
        Foundation = Text("Independent\nSociety of\nKnowledge",
                          font_size=15)
        Foundation.to_corner(RIGHT + UP)
        Introgroup = VGroup(title, Definition, Foundation)
        
        self.add(Foundation)
        self.play(Write(title))
        self.wait()
        self.play(FadeIn(Definition))
        self.wait()
        self.play(FadeOut(Introgroup))
        self.wait(0.5)
        
        
        Intro = Text("1  Introduction",
                     font_size=50)
        Intro.to_edge(UP)
        textofIntro = Text("""One of the best experiment on explaining quantum behaviour is the Stern -
Gerlach experiment, which concerns the spin of a particle like an electron.
It helps us understand that spin is quantized and the concept of collapsing
of a wavefunction
""",
                           font_size=30)
        textofIntro.to_edge(LEFT)
        Introgroup_2 = VGroup(Intro, textofIntro)
        
        #self.add(axes)
        self.play(Write(Intro))
        self.wait()
        self.play(Write(textofIntro, run_time=6))
        self.wait(0.5)
        self.play(FadeOut(Introgroup_2))
        self.wait(0.8)
        
        Experiment = Text("2  The Experiment and Its Setup",
                          font_size=50)
        Experiment.to_edge(UP + LEFT)
        textofExperiment_0 = Text("Stern-Gerlach apparatus was first invented by O. Stern in 1921 and later in",
                                  font_size=30)
        textofExperiment_1 = Text("collaboration with W. Gerlach in 1922; includes one oven of silver atoms",
                                  font_size=30)
        textofExperiment_2 = Text("with a hole on it that atoms can escape through (1) and out of oven",
                                  font_size=30)
        textofExperiment_3 = Text("there exists some beam splitter to make a straight beam of silver atoms",
                                  font_size=30)
        textofExperiment_4 = Text("as (2) in figure (1).", font_size=30)
        textofExperiment_0.to_edge(LEFT)
        textofExperiment_0.shift(2*UP)
        textofExperiment_1.width = textofExperiment_0.width
        textofExperiment_2.width = textofExperiment_1.width
        textofExperiment_3.width = textofExperiment_2.width
        textofExperiment_1.next_to(textofExperiment_0, DOWN, aligned_edge=LEFT)
        textofExperiment_2.next_to(textofExperiment_1, DOWN, aligned_edge=LEFT)
        textofExperiment_3.next_to(textofExperiment_2, DOWN, aligned_edge=LEFT)
        textofExperiment_4.next_to(textofExperiment_3, DOWN, aligned_edge=LEFT)
        textofexperiment_5 = Text("Then this beam is directed to an inhomogeneous magnetic field that two",
                                  font_size=30)
        textofexperiment_6 = Text("magnets with different shapes can produce, as shown in (3).",
                                  font_size=30)
        textofexperiment_5.width = textofExperiment_3. width
        textofexperiment_6.width = textofexperiment_5.width
        textofexperiment_5.next_to(textofExperiment_4, DOWN, aligned_edge=LEFT)
        textofexperiment_6.next_to(textofexperiment_5, DOWN, aligned_edge=LEFT)
        Experimentgroup = VGroup(textofExperiment_0,
                                 textofExperiment_1, textofExperiment_2,
                                     textofExperiment_3, textofExperiment_4,
                                     textofexperiment_5, textofexperiment_6)
                
        textofExperiment_7 = Text("""At last, a screen appears after the magnets, displaying the results of the""",
                                  font_size=30)
        textofExperiment_8 = Text("experiment.", font_size=30)
        textofExperiment_7.to_edge(LEFT, buff=0.8)
        textofExperiment_7.shift(2*UP)
        textofExperiment_7.width = textofExperiment_0.width
        textofExperiment_8.next_to(textofExperiment_7, DOWN, aligned_edge=LEFT)
        Experimentgroup_0 = VGroup(Experiment, textofExperiment_7, textofExperiment_8)
        
        self.wait()
        self.play(Write(textofExperiment_0, run_time=6))
        self.play(Write(textofExperiment_1, run_time=6))
        self.play(Write(textofExperiment_2, run_time=6))
        self.play(Write(textofExperiment_3, run_time=6))
        self.play(Write(textofExperiment_4, run_time=4))
        self.play(Write(textofexperiment_5, run_time=6))
        self.play(Write(textofexperiment_6, run_time=4))
        self.wait()
        self.play(FadeOut(Experimentgroup))
        self.wait()
        self.play(Write(textofExperiment_7))
        self.play(Write(textofExperiment_8))
        self.wait()
        self.play(FadeOut(Experimentgroup_0))
        self.wait(0.8)
        
        Experiment_0 = Text("3  What Stern-Gerlach Experiment Can Tell Us")
        Experiment_0.to_edge(UP + LEFT)
        Experiment_01 = Text("3.1  Spin Is Quantized")
        Experiment_01.next_to(Experiment_0, DOWN, aligned_edge=LEFT)
        textofEXperiment_01 = Text("The silver atoms (Ag) are emoloyed because of their uncoupled electrons (47th)",
                                   font_size=30)
        μtext = MathTex(r"\\vec{\\mu}")
        textofEXperiment_02 = Text("in the last atomic layer (s5) where its intrinsic magnetic moment is {μtext}, so that:",
                                   font_size=30)
        
        self.play(Write(Experiment_0))
        self.play(Write(Experiment_01))
        self.play(Write(textofEXperiment_01))
        self.play(Write(textofEXperiment_02))