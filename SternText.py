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
        group_0123 = VGroup(textofEXperiment_011, textofEXperiment_012,
                            textofEXperiment_013, mathtext_4,
                            textofEXperiment_014, textofEXperiment_015,
                            Experiment_0, Experiment_01)
        
        
        self.play(Write(textofEXperiment_011))
        self.play(Write(textofEXperiment_012))
        self.play(Write(textofEXperiment_013))
        self.play(Write(mathtext_4))
        self.play(Write(textofEXperiment_014))
        self.play(Write(textofEXperiment_015))
        self.wait()
        self.play(FadeOut(group_0123))
        
        
        Experiment_02 = Text("3.2 Sequential Stern-Gerlach Experiment")
        Experiment_02.to_corner(UL)
        Experiment_021 = Text("(Collapsing of Wave Function)",
                              font_size=30)
        Experiment_021.next_to(Experiment_02, DOWN, aligned_edge=LEFT)
        textofEXperiment_016 = Text("The strangest thing about quantum nature is when it occurs that we do",
                                    font_size=30)
        textofEXperiment_016.width = textofEXperiment_011.width
        textofEXperiment_016.next_to(Experiment_021, DOWN, aligned_edge=LEFT)
        textofEXperiment_017 = Text("sequential Stern-Gerlach experiments as we can see in figure (2). We can",
                                    font_size=30)
        textofEXperiment_017.width = textofEXperiment_016.width
        textofEXperiment_017.next_to(textofEXperiment_016, DOWN, aligned_edge=LEFT)
        textofEXperiment_018 = Text("itemize it in 3 ways [1]:", font_size=30)
        textofEXperiment_018.next_to(textofEXperiment_017, DOWN, aligned_edge=LEFT)
        textofEXperiment_019 = Text("1. A beam with state ", font_size=30)
        textofEXperiment_019.next_to(textofEXperiment_018, DOWN, aligned_edge=LEFT)
        mathtext_5 = MathTex("|\psi_0\\rangle")
        mathtext_5.next_to(textofEXperiment_019, RIGHT)
        textofEXperiment_020 = Text("enters to a z axis apparatus then two beam exit", font_size=30)
        textofEXperiment_020.next_to(mathtext_5, RIGHT)
        group_01234 = VGroup(textofEXperiment_019, mathtext_5,
                             textofEXperiment_020,)
        group_01234.width = textofEXperiment_011.width
        group_01234.next_to(textofEXperiment_018, DOWN, aligned_edge=LEFT)
        textofEXperiment_021 = Text("from it with probabilities:", font_size=30)
        textofEXperiment_021.next_to(group_01234, DOWN, aligned_edge=LEFT)
        mathtext_6 = MathTex("P(S_z ^\\pm) = \\langle\\psi_0|P(S_z ^\\pm)\\rangle ^2 =  \\frac{1}{2}")
        mathtext_6.shift(2.2*DOWN)
        group_012345 = VGroup(textofEXperiment_016, textofEXperiment_017,
                               textofEXperiment_018, group_01234,
                               textofEXperiment_021, mathtext_6)
        
        
        self.play(Write(Experiment_02))
        self.play(Write(Experiment_021))
        self.play(Write(textofEXperiment_016))
        self.play(Write(textofEXperiment_017))
        self.play(Write(textofEXperiment_018))
        self.play(Write(group_01234))
        self.play(Write(textofEXperiment_021))
        self.play(Write(mathtext_6))
        self.wait()
        self.play(FadeOut(group_012345))
        
        textofEXperiment_022 = Text("then if we do it again by a second z axis apparatus and just enter the",
                                    font_size=30)
        textofEXperiment_022.width = textofEXperiment_011.width
        textofEXperiment_022.next_to(Experiment_021, DOWN, aligned_edge=LEFT)
        mathtext_7 = MathTex("S_z ^+")
        mathtext_7.next_to(textofEXperiment_022, DOWN, aligned_edge=LEFT)
        textofEXperiment_023 = Text(", we can see that the only", font_size=30)
        textofEXperiment_023.next_to(mathtext_7, RIGHT)
        duplicate = mathtext_7.copy()
        duplicate.next_to(textofEXperiment_023, RIGHT)
        textofEXperiment_024 = Text("component beam exit from the second", font_size=30)
        textofEXperiment_024.next_to(duplicate, RIGHT)
        group_0123456 = VGroup(mathtext_7, textofEXperiment_023,
                               duplicate, textofEXperiment_024)
        group_0123456.width = textofEXperiment_011.width
        group_0123456.shift(0.1*LEFT)
        textofEXperiment_025 = Text("apparatus with probability:", font_size=30)
        textofEXperiment_025.next_to(group_0123456, DOWN, aligned_edge=LEFT)
        mathtext_8 = MathTex("P(S_z ^+) = |\\langle\\psi_0|S_z ^+\\rangle|^2|\\langle S_z ^+|S_z ^+|^2 = \\frac{1}{2}}")
        mathtext_8.shift(0.5*DOWN)
        textofEXperiment_026 = Text("As we expected classically.", font_size=30)
        textofEXperiment_026.next_to(mathtext_8, DOWN)
        textofEXperiment_026.to_edge(LEFT)
        group_01234567 = VGroup(textofEXperiment_022, group_0123456,
                                textofEXperiment_025, mathtext_8,
                                textofEXperiment_026)
        
        
        
        
        
        self.play(Write(textofEXperiment_022))
        self.play(Write(group_0123456))
        self.play(Write(textofEXperiment_025))
        self.play(Write(mathtext_8))
        self.play(Write(textofEXperiment_026))
        self.wait()
        self.play(FadeOut(group_01234567))
        
        
        textofEXperiment_027 = Text("2. As before first a z axis apparatus and then there is a x axis apparatus",
                                    font_size=30)
        textofEXperiment_027.width = textofEXperiment_011.width
        textofEXperiment_027.next_to(Experiment_021, DOWN, aligned_edge=LEFT)
        textofEXperiment_028 = Text("on the way of", font_size=30)
        textofEXperiment_028.next_to(textofEXperiment_027, DOWN, aligned_edge=LEFT)
        duplicate_0 = duplicate.copy()
        duplicate_0.next_to(textofEXperiment_028, RIGHT)
        textofExperiment_029 = Text("component beam, the final result is two beams of", font_size=30)
        textofExperiment_029.next_to(duplicate_0, RIGHT)
        mathtext_9 = MathTex("S_z ^\\pm")
        mathtext_9.next_to(textofExperiment_029, RIGHT)
        textofExperiment_030 = Text("components with probability:", font_size=30)
        group_012345678 = VGroup(textofEXperiment_028, duplicate_0,
                                 textofExperiment_029, mathtext_9)
        group_012345678.width = textofEXperiment_027.width
        textofExperiment_030.next_to(group_012345678, DOWN, aligned_edge=LEFT)
        mathtext_10 = MathTex("P(S_z ^\\pm) = |\\langle\\psi_0|S_z ^+\\rangle|^2 |\\langle S_z ^+|S_z ^\\pm \\rangle|^2 = \\frac{1}{4}")
        mathtext_10.shift(0.2*DOWN)
        textofExperiment_031 = Text("as we expected.", font_size=30)
        textofExperiment_031.next_to(mathtext_10, DOWN, aligned_edge=LEFT)
        textofExperiment_031.to_edge(LEFT)
        group_0123456789 = VGroup(textofEXperiment_027, group_012345678,
                                  textofExperiment_030, mathtext_10,
                                  textofExperiment_031)
        
        self.play(Write(textofEXperiment_027))
        self.play(Write(group_012345678))
        self.play(Write(textofExperiment_030))
        self.play(Write(mathtext_10))
        self.play(Write(textofExperiment_031))
        self.wait()
        self.play(FadeOut(group_0123456789))
        
        
        textofEXperiment_032 = Text("3. Finally doing the same as item no.2 just after the x axis apparatus",
                                    font_size=30)
        textofEXperiment_032.width = textofEXperiment_011.width
        textofEXperiment_032.next_to(Experiment_021, DOWN, aligned_edge=LEFT)
        textofEXperiment_033 = Text("on the way of", font_size=30)
        textofEXperiment_033.next_to(textofEXperiment_032, DOWN, aligned_edge=LEFT)
        mathtext_11 = MathTex("S_z ^x")
        mathtext_11.next_to(textofEXperiment_033, RIGHT)
        textofEXperiment_034 = Text("beam, before going further we can deduce logically that",
                                    font_size=30)
        textofEXperiment_034.next_to(mathtext_11, RIGHT)
        group_010 = VGroup(textofEXperiment_033, mathtext_11,
                           textofEXperiment_034)
        group_010.width = textofEXperiment_032.width
        textofEXperiment_035 = Text("like as item no.1 the only beam from the z axis apparatus is",
                                    font_size=30)
        textofEXperiment_035.next_to(group_010, DOWN, aligned_edge=LEFT)
        mathtext_12 = MathTex("S_z ^+")
        mathtext_12.next_to(textofEXperiment_035, RIGHT)
        textofEXperiment_036 = Text(", but in the", font_size=30)
        textofEXperiment_036.next_to(mathtext_12, RIGHT)
        group_013 = VGroup(textofEXperiment_035, mathtext_12,
                           textofEXperiment_036)
        group_013.width = textofEXperiment_032.width
        group_013.next_to(textofEXperiment_033, DOWN, aligned_edge=LEFT)
        textofEXperiment_037 = Text("our classical logic is not correct; the real and strangest result for us",
                                    font_size=30)
        textofEXperiment_037.width = textofEXperiment_032.width
        textofEXperiment_037.next_to(textofEXperiment_035, DOWN, aligned_edge=LEFT)
        textofEXperiment_038 = Text("occurs in such a way that we have two beams with",
                                    font_size=30)
        textofEXperiment_038.next_to(textofEXperiment_037, DOWN, aligned_edge=LEFT)
        mathtext_13 = MathTex("S_z ^\\pm")
        mathtext_13.next_to(textofEXperiment_038, RIGHT)
        textofEXperiment_039 = Text("components with", font_size=30)
        textofEXperiment_039.next_to(mathtext_13, RIGHT)
        group_014 = VGroup(textofEXperiment_038, mathtext_13,
                           textofEXperiment_039)
        group_014.width = textofEXperiment_037.width
        textofEXperiment_040 = Text("probability as below:", font_size=30)
        textofEXperiment_040.next_to(group_014, DOWN, aligned_edge=LEFT)
        mathtext_14 = MathTex("P(S_z ^+) = |\\langle\\psi_o|S_z ^+\\rangle|^2 |\\langle S_z ^+|S_z ^+\\rangle|^2 |\\rangle S_z ^+|S_z ^\\pm\\rangle| = \\frac{1}{8}")
        mathtext_14.shift(2.5*DOWN)
        group_015 = VGroup(textofEXperiment_032, group_010,
                           group_013, textofEXperiment_037,
                           group_014, textofEXperiment_040,
                           mathtext_14)
        
        
        
        self.play(Write(textofEXperiment_032))
        self.play(Write(group_010))
        self.play(Write(textofEXperiment_035))
        self.play(Write(mathtext_12))
        self.play(Write(textofEXperiment_036))
        self.play(Write(textofEXperiment_037))
        self.play(Write(group_014))
        self.play(Write(textofEXperiment_040))
        self.play(Write(mathtext_14))
        self.wait()
        self.play(FadeOut(group_015))
        
        
        textofEXperiment_041 = Text("This is what we call it collapsing of the wave function or better say any",
                                    font_size=30)
        textofEXperiment_041.width = textofEXperiment_011.width
        textofEXperiment_041.next_to(Experiment_021, DOWN, aligned_edge=LEFT)
        textofEXperiment_042 = Text("observation on quantum systems perturbed the results and the different",
                                    font_size=30)
        textofEXperiment_042.width = textofEXperiment_041.width
        textofEXperiment_042.next_to(textofEXperiment_041, DOWN, aligned_edge=LEFT)
        textofEXperiment_043 = Text("apparatus collapses the first wave function then if we do experiment with",
                                    font_size=30)
        textofEXperiment_043.width = textofEXperiment_042.width
        textofEXperiment_043.next_to(textofEXperiment_042, DOWN, aligned_edge=LEFT)
        textofEXperiment_044 = Text("the first apparatus make a new wave function, which is unknown to us in",
                                    font_size=30)
        textofEXperiment_044.width = textofEXperiment_043.width
        textofEXperiment_044.next_to(textofEXperiment_043, DOWN, aligned_edge=LEFT)
        textofEXperiment_045 = Text("classical physics because it's a quantum behavior!", font_size=30)
        textofEXperiment_045.next_to(textofEXperiment_044, DOWN, aligned_edge=LEFT)
        group_016 = VGroup(Experiment_02, Experiment_021,
                           textofEXperiment_041, textofEXperiment_042,
                           textofEXperiment_043, textofEXperiment_044,
                           textofEXperiment_045)
        
        self.play(Write(textofEXperiment_041))
        self.play(Write(textofEXperiment_042))
        self.play(Write(textofEXperiment_043))
        self.play(Write(textofEXperiment_044))
        self.play(Write(textofEXperiment_045))
        self.wait()
        self.play(FadeOut(group_016))
        
        Experiment_03 = Text("4 Conclusion")
        Experiment_03.to_corner(UL)
        textofEXperiment_046 = Text("We can see in this brief text that Stern_Gerlach experiment shows us the",
                                    font_size=30)
        textofEXperiment_046.width = textofEXperiment_011.width
        textofEXperiment_046.next_to(Experiment_03, DOWN, aligned_edge=LEFT)
        textofEXperiment_047 = Text("Spin of a quantum particle is quantized and the sequential Stern-Gerlach",
                                    font_size=30)
        textofEXperiment_047.width = textofEXperiment_046.width
        textofEXperiment_047.next_to(textofEXperiment_046, DOWN, aligned_edge=LEFT)
        textofEXperiment_048 = Text("experiment changes our classical thoughts with its amazing results.",
                                    font_size=30)
        textofEXperiment_048.next_to(textofEXperiment_047, DOWN, aligned_edge=LEFT)
        References = Text("References")
        References.next_to(textofEXperiment_048, DOWN, aligned_edge=LEFT)
        Referencetext_1 = Text("[1] Jean Bricmont. Making sense of Quantum Mechanics . Springer, 2016", font_size=30)
        Referencetext_1.width = textofEXperiment_011.width
        Referencetext_1.next_to(References, DOWN, aligned_edge=LEFT)
        Referencetext_2 = Text("[2] j.j. Sakurai and Jim Napolitano. Modern Quantum Mechanics. Cmabridge ", font_size=30)
        Referencetext_2.width = Referencetext_1.width
        Referencetext_2.next_to(Referencetext_1, DOWN, aligned_edge=LEFT)
        Referencetext_21 = Text("University Press, 2020", font_size=30)
        Referencetext_21.next_to(Referencetext_2, DOWN, aligned_edge=LEFT)
        group_017 = VGroup(Experiment_03, textofEXperiment_046,
                           textofEXperiment_047, textofEXperiment_048,
                           References, Referencetext_1,
                           Referencetext_2, Referencetext_21)
        ENDING = Text("ISK")
        
        self.play(Write(Experiment_03))
        self.play(Write(textofEXperiment_046))
        self.play(Write(textofEXperiment_047))
        self.play(Write(textofEXperiment_048))
        self.wait(0.8)
        self.play(Write(References))
        self.play(Write(Referencetext_1))
        self.play(Write(Referencetext_2))
        self.play(Write(Referencetext_21))
        self.wait()
        self.play(FadeOut(group_017))
        self.play(FadeIn(ENDING, run_time=4))