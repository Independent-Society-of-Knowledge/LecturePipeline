import yaml
from typing import Any

from PIL import ImageFont


def typography(key: str, default: Any = None):
        """
        Initialize CourseConfig with the path to the YAML file.

        :param file_path: Path to the YAML configuration file.
        """
        file_path = "lecturePipeline/typography/fonts/typography.yml"
        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")
        keys = key.split('.')
        value = data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

            if value is None:
                return default

        return value


def calculate_text_width(text, font_size, font_name="lecturePipeline/typography/fonts/IBM_Plex_Sans/IBMPlexSans-Light.ttf"):
    """Calculate the width of text in pixels."""
    try:
        font = ImageFont.truetype(font_name, font_size)
        # Using getbbox() which returns (left, top, right, bottom)
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]  # right - left = width
    except OSError:
        # Fallback if font file not found
        print(f"Warning: Font {font_name} not found. Using default.")
        font = ImageFont.load_default()
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]


def split_text_to_width(text: str, max_width: float, font_size: int, font_name="IBM Plex Sans") -> list[str]:
    """Split text into lines that fit within max_width."""
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_width = calculate_text_width(word, font_size, font_name)
        space_width = calculate_text_width(" ", font_size, font_name)

        # Check if adding this word would exceed max_width
        if current_width + word_width + (space_width if current_line else 0) <= max_width:
            current_line.append(word)
            current_width += word_width + (space_width if current_line else 0)
        else:
            # Start a new line
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width

    # Add the last line if it exists
    if current_line:
        lines.append(" ".join(current_line))

    return lines

def computeLineSpacing(fontSize, lineHeightMultiplier, lineSpacingMultiplier):

    return 2.38 * ((lineHeightMultiplier - fontSize) * (1 + lineSpacingMultiplier) + fontSize)


def calculate_scaling_factor(font_size, desired_height, font_path="lecturePipeline/typography/fonts/IBM_Plex_Sans/IBMPlexSans-Light.ttf"):
        font = ImageFont.truetype(font_path, font_size)
        ascent, descent = font.getmetrics()
        total_height = ascent + descent
        scaling_factor = desired_height / total_height
        return scaling_factor

if __name__ == "__main__":
    print(calculate_scaling_factor(32, 100))






