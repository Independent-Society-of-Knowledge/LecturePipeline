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
        
        self.play(Write(Experiment))
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
                                   font_size=27)
        textofEXperiment_01.next_to(Experiment_01, DOWN, aligned_edge=LEFT)
        textofEXperiment_02 = Text("in the last atomic layer (s5) where its intrinsic magnetic moment is",
                                   font_size=27)
        textofEXperiment_02.width = textofEXperiment_01.width
        textofEXperiment_02.next_to(textofEXperiment_01, DOWN, aligned_edge=LEFT)
        mu = MathTex("\\vec{\\mu}")
        mu.next_to(textofEXperiment_02, DOWN, aligned_edge=LEFT)
        textofEXperiment_03 = Text(", so that:", font_size=30)
        textofEXperiment_03.next_to(mu, RIGHT)
        groupmu_03 = VGroup(mu, textofEXperiment_03)
        mathtext_0 = MathTex("\\vec{\\mu} \\propto \\vec{S}")
        mathtext_0.shift(0.7*DOWN)
        textofEXperiment_04 = Text("Then according to Hamiltonian of interaction between the intrinsic magnetic moment",
                                   font_size=30)
        textofEXperiment_04.width = textofEXperiment_02.width
        textofEXperiment_04.to_edge(LEFT)
        textofEXperiment_04.shift(1.7*DOWN)
        textofEXperiment_05 = Text("of electron and magnetic field",
                                   font_size=30)
        mathtext_1 = MathTex("(H=-\\vec{\\mu} \\cdot \\vec{B})")
        mathtext_1.next_to(textofEXperiment_05, RIGHT)
        textofEXperiment_06 = Text(", if the B is directed to z",
                                   font_size=30)
        textofEXperiment_06.next_to(mathtext_1, RIGHT)
        group_0 = VGroup(textofEXperiment_05, mathtext_1,textofEXperiment_06)
        group_0.width = textofEXperiment_04.width
        group_0.next_to(textofEXperiment_04, DOWN, aligned_edge=LEFT)
        group_01 = VGroup(textofEXperiment_01, textofEXperiment_02,
                          mu, textofEXperiment_03,
                          mathtext_0, textofEXperiment_04,
                          group_0)
        textofEXperiment_07 = Text("axis, this electron experiences a force:",
                                   font_size=30)
        textofEXperiment_07.next_to(Experiment_01, DOWN, aligned_edge=LEFT)
        mathtext_2 = MathTex("F_{z} = \\frac{\\partial}{\\partial z} \left( \\vec{\\mu} \\cdot \\vec{B} \\right) \\approx \\mu_{z} \\frac{\\partial B_{z}}{\\partial z}")
        textofEXperiment_08  = Text("According to classical physics, the magnetic moment of an electron must be ",
                                    font_size=30)
        textofEXperiment_08.width = textofEXperiment_01.width
        textofEXperiment_08.next_to(mathtext_2, DOWN)
        textofEXperiment_08.to_edge(LEFT)
        mathtext_3 = MathTex("-a < \\mu_{z} < a")
        mathtext_3.next_to(textofEXperiment_08, DOWN)
        mathtext_3.to_edge(LEFT)
        textofEXperiment_09 = Text("or continuous value, then under the above force we can ",
                                   font_size=30)
        textofEXperiment_09.next_to(mathtext_3, RIGHT, buff=0.5)
        textofEXperiment_010 = Text("see that the (4) pattern in figure 1 must be shown to us. But the real result is",
                                    font_size=30)
        textofEXperiment_010.width = textofEXperiment_01.width
        textofEXperiment_010.next_to(mathtext_3, DOWN, aligned_edge=LEFT)
        group_012 = VGroup(textofEXperiment_07, textofEXperiment_08,
                           textofEXperiment_09, textofEXperiment_010,
                           mathtext_2, mathtext_3)
        
        self.play(Write(Experiment_0))
        self.play(Write(Experiment_01))
        self.play(Write(textofEXperiment_01))
        self.play(Write(textofEXperiment_02))
        self.play(Write(groupmu_03))
        self.play(Write(mathtext_0))
        self.play(Write(textofEXperiment_04))
        self.play(Write(textofEXperiment_05))
        self.play(Write(mathtext_1))
        self.play(Write(textofEXperiment_06))
        self.wait(0.5)
        self.play(FadeOut(group_01))
        self.wait()
        self.play(Write(textofEXperiment_07))
        self.play(Write(mathtext_2))
        self.play(Write(textofEXperiment_08))
        self.play(Write(mathtext_3))
        self.play(Write(textofEXperiment_09))
        self.play(Write(textofEXperiment_010))
        self.wait()
        self.play(FadeOut(group_012))
        
        
        textofEXperiment_011 = Text("different; the (5) pattern in figure 1 appears! So we can deduce from this results",
                                    font_size=30)
        textofEXperiment_011.width = textofEXperiment_010.width
        textofEXperiment_011.next_to(Experiment_01, DOWN, aligned_edge=LEFT)
        textofEXperiment_012 = Text("that the magnetic moment or intrinsic spin of electron must be a discrete value",
                                    font_size=30)
        textofEXperiment_012.width = textofEXperiment_011.width
        textofEXperiment_012.next_to(textofEXperiment_011, DOWN, aligned_edge=LEFT)
        textofEXperiment_013 = Text("which is: ", font_size=30)
        textofEXperiment_013.next_to(textofEXperiment_012, DOWN, aligned_edge=LEFT)
        mathtext_4 = MathTex("S_{z} = \\pm \\frac{\\hbar}{2}.", font_size=40)
        mathtext_4.next_to(textofEXperiment_013, RIGHT)
        textofEXperiment_014 = Text("Then the most important result of Stern-Gerlach experiment is that the electron ",
                                    font_size=30)
        textofEXperiment_014.width = textofEXperiment_012.width
        textofEXperiment_014.next_to(textofEXperiment_013, DOWN, aligned_edge=LEFT)
        textofEXperiment_015 = Text("has spin and its value is discrete or better to say that Spin Is Quantized.",
                                    font_size=30)
        textofEXperiment_015.next_to(textofEXperiment_014, DOWN, aligned_edge=LEFT)
        
        
        self.play(Write(textofEXperiment_011))
        self.play(Write(textofEXperiment_012))
        self.play(Write(textofEXperiment_013))
        self.play(Write(mathtext_4))
        self.play(Write(textofEXperiment_014))
        self.play(Write(textofEXperiment_015))
        self.wait()
        
        Experiment_02 = Text("3.2 Sequential Stern-Gerlach Experiment")
        Experiment_02.to_corner(UL)
        Experiment_021 = Text("(Collapsing of Wave Function)",
                              font_size=30)
        Experiment_021.next_to(Experiment_02, RIGHT, buff=0.3)
        
        self.play(Write(Experiment_02))
        self.play(Write(Experiment_021))
        self.wait()