from manim import *

from lecturePipeline.configuration.lecture_configuration import LectureConfiguration
from lecturePipeline.scenes.title_scenes.left_full import  leftFull
from lecturePipeline.scenes.title_scenes.right_full import rightFull
from lecturePipeline.typography.text import textHandler
from lecturePipeline.utils.percent_to_units import percent_to_units
from lecturePipeline.utils.time_manager import time_manager


class TitleScene(Scene):
    def __init__(self, configuration: LectureConfiguration = LectureConfiguration(
        "/home/kid-a/Documents/isk/LecturePipeline/resources/testconf.yml"),
                 title: str = "Title",
                 subtitle: str = "Subtitle",
                 placement: str = "right-full",
                 duration: float = 4
                 ):
        super().__init__()

        # Setting Lecture Configurations
        self.lectureConfig = configuration
        config.frame_width = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[0]
        config.frame_height = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[1]
        self.camera.frame_width = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[0]
        self.camera.frame_height = self.lectureConfig.get("lecture.metadata.video-generation.ratio")[1]

        # Stacking Arguments for video production
        self.title = title
        self.subtitle = subtitle
        self.placement = placement
        self.duration = duration


    def construct(self):
        if self.placement == "left-full":
            scene = leftFull(configuration=self.lectureConfig, title=self.title, subtitle=self.subtitle,
                                 duration=self.duration).construct(self)
        elif self.placement == "right-full":
            scene =  rightFull(configuration=self.lectureConfig, title=self.title, subtitle=self.subtitle,
                                  duration=self.duration).construct(self)

        self.wait(4)

