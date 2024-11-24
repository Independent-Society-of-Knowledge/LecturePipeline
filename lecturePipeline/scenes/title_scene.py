from manim import *
from networkx.readwrite.gml import literal_stringizer

from lecturePipeline.configuration.lecture_configuration import LectureConfiguration
from lecturePipeline.typography.text import textHandler
from lecturePipeline.utils.percent_to_units import percent_to_units


class TitleScene(Scene):
    def __init__(self, configuration: LectureConfiguration = LectureConfiguration(
        "/home/kid-a/Documents/isk/LecturePipeline/resources/testconf.yml"), title: str = "Title",
                 subtitle: str = "Subtitle"):
        super().__init__()
        # Setting Lecture Configurations
        self.lectureConfig = configuration
        config.frame_width = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[0]
        config.frame_height = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[1]
        self.camera.frame_width = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[0]
        self.camera.frame_height = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[1]

        # Stacking Lecutre Title and Subtitle
        self.title = self.lectureConfig.get("lecture.metadata.title")
        print(self.title)
        self.subtitle = self.lectureConfig.get("lecture.metadata.subtitle")
        self.placement = self.lectureConfig.get("lecture.scene-configurations.title-scene.placement")

    def construct(self):
        background = ImageMobject(
            self.lectureConfig.get("lecture.scene-configurations.title-scene.background")).scale_to_fit_depth(1.0)

        rectangle = Rectangle(width=percent_to_units(60, config), height=percent_to_units(100, config), fill_color=BLACK, fill_opacity=0.6, stroke_width=0).move_to(LEFT * 3,
                                                                                                           aligned_edge=LEFT).move_to(LEFT * 8, aligned_edge=LEFT)

        self.add(background)
        self.play(Transform(Rectangle(width=0,height=percent_to_units(100, config), stroke_width=0, fill_opacity=0).move_to(LEFT *8, aligned_edge=LEFT),rectangle))
        textWidth = 120
        title = textHandler(
            input=self.title,
            type="fluid.display-03-mx",
            config=config,
            width=textWidth,
            position=LEFT * 7.5 + UP * 1.8
        )
        subtitle = textHandler(
            input=self.subtitle,
            type="fluid.paragraph-01-mx",
            config=config,
            width=textWidth,
            position=LEFT * 7.5 + DOWN * 1.8)

        for t in title:
            # self.add(t)
            self.play(
                Write(t),
                run_time=2)

        for s in subtitle:
            # self.add(s)
            self.play(
                Write(s,
                      run_time=2))

        self.wait(4)
