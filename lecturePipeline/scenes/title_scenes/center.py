from lecturePipeline import LectureConfiguration
from manim import *
from lecturePipeline.typography.text import textHandler
from lecturePipeline.utils.percent_to_units import percent_to_units
from lecturePipeline.utils.time_manager import time_manager

def center(configuration: LectureConfiguration = LectureConfiguration("/home/kid-a/Documents/isk/LecturePipeline/resources/testconf.yml"),
                title: str = "Title",
                 subtitle: str = "Subtitle",
                 duration: float = 4
                 ):
    class CenterScene(Scene):
        def setup(self):
            self.title = title
            self.subtitle = subtitle
            self.duration = duration
            self.configuration = configuration
        def construct(self):
            config.frame_width = self.configuration.get("lecture.metadata.video-generation.ratio")[0]
            config.frame_height = self.configuration.get("lecture.metadata.video-generation.ratio")[1]
            self.camera.frame_width = self.configuration.get("lecture.metadata.video-generation.ratio")[0]
            self.camera.frame_height = self.configuration.get("lecture.metadata.video-generation.ratio")[1]
            self.perSectionTime = time_manager(3, self.duration)['perSectionTime']
            background = ImageMobject(
                self.configuration.get("lecture.scene-configurations.title-scene.background")).scale_to_fit_depth(1.0)

            rectangle = Rectangle(width=percent_to_units(50, config), height=percent_to_units(60, config, dimension="height"),
                                  fill_color=BLACK, fill_opacity=1, stroke_width=0)


            self.add(background)
            self.play(Transform(
                Rectangle(width=percent_to_units(50, config), height=0, stroke_width=0, fill_opacity=0),
                rectangle), run_time=1)
            textWidth = 120
            title = textHandler(
                input=self.title,
                type="fluid.display-03-xl",
                config=config,
                width=textWidth,
                position=LEFT * percent_to_units(20, config) + UP * 1.8,
                alignment=LEFT
            )
            subtitle = textHandler(
                input=self.subtitle,
                type="fluid.paragraph-01-xl",
                config=config,
                width=textWidth,
                position=LEFT * percent_to_units(20, config) + DOWN * 1.8,
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

    return CenterScene

