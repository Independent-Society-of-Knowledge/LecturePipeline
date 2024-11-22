from manim import *


class PrimaryColor:
    def __init__(self):
        self.name = "primary"
        self.colors = {
            "10":  ManimColor("#240B43"),
            "9":  ManimColor("#381366"),
            "8":  ManimColor("#4B2578"),
            "7":  ManimColor("#5D3689"),
            "6":  ManimColor("#6F489A"),
            "5":  ManimColor("#8159AB"),
            "4":  ManimColor("#A57CCD"),
            "3":  ManimColor("#C99EEF"),
            "2":  ManimColor("#D9BCF3"),
            "1": ManimColor("#F2E2FF")}
    
    def get(self, num: int) :
        return self.colors[str(num)]
class DarkColor:
    def __init__(self):
        self.name = "dark"
        self.colors = {
            "1": ManimColor("#000000"),
            "2": ManimColor("#060606"),
            "3": ManimColor("#0C0C0C"),
            "4": ManimColor("#181818"),
            "5": ManimColor("#242424"),
            "6": ManimColor("#303030"),
            "7": ManimColor("#3C3C3C"),
            "8": ManimColor("#484848"),
            "9": ManimColor("#545454"),
            "10": ManimColor("#606060")}
    def get(self, num: int) :
        return self.colors[str(num)]

class LightColor:
    def __init__(self):
        self.name = "light"
        self.colors = {
            "10": ManimColor("#717171"),
            "9": ManimColor("#888888"),
            "8": ManimColor("#9C9C9C"),
            "7": ManimColor("#C7C7C7"),
            "6": ManimColor("#B0B0B0"),
            "5": ManimColor("#D8D8D8"),
            "4": ManimColor("#ECECEC"),
            "3": ManimColor("#F6F6F6"),
            "2": ManimColor("#FAFAFA"),
            "1": ManimColor("#FFFFFF")}
    def get(self, num: int) :
        return self.colors[str(num)]

def getColor(name: str, num: int) :
    """
    Give a name (primary, dark, light) and a number (10, 20, 30, 40, ..., 100) to get the corresponding color value.
    @return color value in hex (string) without the sharp.
    """
    primary = PrimaryColor()
    dark = DarkColor()
    light = LightColor()
    if name == "primary":
        return primary.get(num)
    elif name == "dark":
        return dark.get(num)
    elif name == "light":
        return light.get(num)
    else:
        return "No-Color-Found"
