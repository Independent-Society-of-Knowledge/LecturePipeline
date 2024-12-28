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
        # print(f"Warning: Font {font_name} not found. Using default.")
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

def split_text_to_char_number_loosely(text: str, char_num: float) -> list[str]:
    """Split text into lines that has equal number of characters."""
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_width = len(word)
        space_width = 1

        # Check if adding this word would exceed max_width
        if current_width + word_width + (space_width if current_line else 0) <= char_num:
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


def split_text_to_char_number_strictly(text: str, char_num: float) -> list[str]:
    """Split text into lines with a strict character limit,
    breaking words with a hyphen if they exceed the limit."""
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        # If the entire word is longer than char_num
        if len(word) > char_num:
            # Break the long word
            for i in range(0, len(word), char_num):
                # Last segment
                if i + char_num >= len(word):
                    segment = word[i:]
                    # If current line has space, add to current line
                    if current_line and current_width + len(segment) + 1 <= char_num:
                        current_line.append(segment)
                        current_width += len(segment) + 1
                    else:
                        # Start new line
                        if current_line:
                            lines.append(" ".join(current_line))
                        current_line = [segment]
                        current_width = len(segment)
                else:
                    # Middle segments
                    segment = word[i:i+char_num] + "-"
                    # If current line has space, add to current line
                    if current_line and current_width + len(segment) + 1 <= char_num:
                        current_line.append(segment)
                        current_width += len(segment) + 1
                    else:
                        # Start new line
                        if current_line:
                            lines.append(" ".join(current_line))
                        current_line = [segment]
                        current_width = len(segment)
        else:
            # Normal word handling
            # Check if adding this word would exceed max_width
            if current_width + len(word) + (1 if current_line else 0) <= char_num:
                current_line.append(word)
                current_width += len(word) + (1 if current_line else 0)
            else:
                # Start a new line
                lines.append(" ".join(current_line))
                current_line = [word]
                current_width = len(word)

    # Add the last line if it exists
    if current_line:
        lines.append(" ".join(current_line))

    return lines

def split_text_to_char_number(text: str, char_num: float, loosely: bool = False) -> list[str]:
    if loosely:
        return split_text_to_char_number_loosely(text, char_num)
    else:
        return split_text_to_char_number_strictly(text, char_num)
if __name__ == "__main__":
    l1 = r"""
In quantum mechanics, the **Schrödinger equation** is a fundamental equation that describes how the quantum state of a physical system changes with time. The time-dependent form of the Schrödinger equation is given by 
$$ i\hbar \frac{\partial}{\partial t} \psi(x, t) = \hat{H} \psi(x, t), $$ 
where $ \psi(x, t) $ is the wavefunction of the system, $ \hbar $ is the reduced Planck's constant, and $ \hat{H} $ is the Hamiltonian operator. For a particle in a one-dimensional potential $ V(x) $, the Hamiltonian is expressed as 
$$ \hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x). $$
In the case of a **free particle**, where $ V(x) = 0 $, the equation simplifies to:
$$ i\hbar \frac{\partial}{\partial t} \psi(x, t) = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi(x, t). $$
The solution to this equation can be expressed as a **plane wave**:
$$ \psi(x, t) = A e^{i(kx - \omega t)}, $$ 
where $ A $ is the amplitude, $ k $ is the wave number, and $ \omega $ is the angular frequency, related by the dispersion relation $ \omega = \frac{\hbar k^2}{2m} $."""
    resutls = split_text_to_width(l1, 200, 32)
    print(resutls)
    for r in resutls:
        print(r.split("$"))
    # print(split_text_to_width(l2, 90, 32))
    # print(split_text_to_width(l3, 90, 32))






