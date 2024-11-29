from manim import *

from lecturePipeline.configuration.lecture_configuration import LectureConfiguration
from lecturePipeline.scenes.title_scenes.center import center
from lecturePipeline.scenes.title_scenes.left_compact import leftCompact
from lecturePipeline.scenes.title_scenes.left_full import  leftFull
from lecturePipeline.scenes.title_scenes.right_compact import rightCompact
from lecturePipeline.scenes.title_scenes.right_full import rightFull



class TitleScene(Scene):
    def __init__(self, configuration: LectureConfiguration = LectureConfiguration(
        "/home/kid-a/Documents/isk/LecturePipeline/resources/testconf.yml"),
                 title: str = "Title of a lecture that is a long title indeed",
                 subtitle: str = "Subtitle of a lecture that is a long subtitle indeed",
                 placement: str = "right-full",
                 duration: float = 4
                 ):
        super().__init__()

        # Setting Lecture Configurations
        self.configuration = configuration
        config.frame_width = self.configuration.get("lecture.metadata.video-generation.ratio")[0]
        config.frame_height = self.configuration.get("lecture.metadata.video-generation.ratio")[1]
        self.camera.frame_width = self.configuration.get("lecture.metadata.video-generation.ratio")[0]
        self.camera.frame_height = self.configuration.get("lecture.metadata.video-generation.ratio")[1]

        # Stacking Arguments for video production
        self.title = title
        self.subtitle = subtitle
        self.placement = placement
        self.duration = duration


    def construct(self):
        if self.placement == "left-full":
            scene = leftFull(configuration=self.configuration, title=self.title, subtitle=self.subtitle,
                                 duration=self.duration).construct(self)
        elif self.placement == "right-full":
            scene =  rightFull(configuration=self.configuration, title=self.title, subtitle=self.subtitle,
                                  duration=self.duration).construct(self)
        elif self.placement == "center":
            scene = center(configuration=self.configuration, title=self.title, subtitle=self.subtitle, duration=self.duration).construct(self)
        elif self.placement == "right-compact":
            scene =  rightCompact(configuration=self.configuration, title=self.title, subtitle=self.subtitle,
                                  duration=self.duration).construct(self)
        elif self.placement == "left-compact":
            scene = leftCompact(configuration=self.configuration, title=self.title, subtitle=self.subtitle, duration=self.duration).construct(self)
        self.wait(4)

