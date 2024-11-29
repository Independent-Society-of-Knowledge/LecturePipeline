from lecturePipeline import LectureConfiguration
from manim import *
from lecturePipeline.typography.text import textHandler
from lecturePipeline.utils.percent_to_units import percent_to_units
from lecturePipeline.utils.time_manager import time_manager

def rightFull(configuration: LectureConfiguration = LectureConfiguration(
        "/home/kid-a/Documents/isk/LecturePipeline/resources/testconf.yml"),
                 title: str = "Title",
                 subtitle: str = "Subtitle",
                 duration: float = 4
                 ):
    class RightFullScene(Scene):

        def setup(self):
            # Setting Lecture Configurations
            self.configuration = configuration
            config.frame_width = self.configuration.get("lecture.metadata.video-generation.ratio")[0]
            config.frame_height = self.configuration.get("lecture.metadata.video-generation.ratio")[1]
            self.camera.frame_width = self.configuration.get("lecture.metadata.video-generation.ratio")[0]
            self.camera.frame_height = self.configuration.get("lecture.metadata.video-generation.ratio")[1]

            # Stacking Arguments for video production
            self.title = title
            self.subtitle = subtitle
            self.duration = duration


        def construct(self):
            background = ImageMobject(
                self.configuration.get("lecture.scene-configurations.title-scene.background")).scale_to_fit_depth(1.0)

            rectangle = Rectangle(width=percent_to_units(60, config), height=percent_to_units(100, config),
                                  fill_color=BLACK, fill_opacity=1, stroke_width=0).move_to(
                RIGHT * 8, aligned_edge=RIGHT)
            self.perSectionTime = time_manager(3, self.duration)['perSectionTime']

            self.add(background)
            self.play(Transform(
                Rectangle(width=0, height=percent_to_units(100, config), stroke_width=0, fill_opacity=0).move_to(RIGHT * 8,
                                                                                                                 aligned_edge=RIGHT),
                rectangle), background.animate.move_to(LEFT * 2), run_time=1)
            titleTextWidth = 90
            subtitleTextWidth = 200
            title = textHandler(
                input=self.title,
                type="fluid.display-03-mx",
                config=config,
                width=titleTextWidth,
                position=LEFT * percent_to_units(5, config)  + UP * 1.8,
                alignment=LEFT
            )
            subtitle = textHandler(
                input=self.subtitle,
                type="fluid.paragraph-01-mx",
                config=config,
                width=subtitleTextWidth,
                position=LEFT * percent_to_units(5, config)  + DOWN * 1.8,
                alignment=LEFT
            )

            for t in title:
                # self.add(t)
                self.play(
                    Write(t),
                    run_time=self.perSectionTime)

            for s in subtitle:
                # self.add(s)
                self.play(
                    Write(s,
                          run_time=self.perSectionTime))
    return RightFullScene
