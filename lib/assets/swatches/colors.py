class PrimaryColor:
    def __init__(self):
        self.name = "primary"
        self.colors = {
            "10":  "240B43",
            "20":  "381366",
            "30":  "4B2578",
            "40":  "5D3689",
            "50":  "6F489A",
            "60":  "8159AB",
            "70":  "A57CCD",
            "80":  "C99EEF",
            "90":  "D9BCF3",
            "100": "F2E2FF"}
    
    def get(self, num: int) -> str :
        return self.colors[str(num)]
class DarkColor:
    def __init__(self):
        self.name = "dark"
        self.colors = {
            "10": "000000",
            "20": "060606",
            "30": "0C0C0C",
            "40": "181818",
            "50": "242424",
            "60": "303030",
            "70": "3C3C3C",
            "80": "484848",
            "90": "545454",
            "100": "606060"}
    def get(self, num: int) -> str :
        return self.colors[str(num)]

class LightColor:
    def __init__(self):
        self.name = "light"
        self.colors = {
            "100": "717171",
            "90": "888888",
            "80": "9C9C9C",
            "70": "C7C7C7",
            "60": "B0B0B0",
            "50": "D8D8D8",
            "40": "ECECEC",
            "30": "F6F6F6",
            "20": "FAFAFA",
            "10": "FFFFFF"}
    def get(self, num: int) -> str :
        return self.colors[str(num)]

def getColor(name: str, num: int) -> str :
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
if __name__ =="__main__":
    swatchNums = [10,20,30,40,50,60,70,80,90,100]
    swatchNames = ["primary","dark","light"]
    for name in swatchNames:
        for num in swatchNums:
            print(f"{name} - {num}: {getColor(name, num)}")
    
