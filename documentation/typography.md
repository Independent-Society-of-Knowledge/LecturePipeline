# Typography Utility Module Documentation

## Overview
This module provides advanced typography management tools for the ISK LecturePipeline, offering comprehensive text processing and font-related utilities.

## Functions

### 1. `typography(key: str, default: Any = None)`
Retrieves typography configuration from a YAML file.

#### Parameters
- `key` (str): Dot-separated configuration key
- `default` (Any, optional): Default value if key not found

#### Returns
- Configuration value
- Default value if key is not found

#### Behavior
- Loads configuration from `lecturePipeline/typography/fonts/typography.yml`
- Supports nested key lookup
- Handles file not found and YAML parsing errors

### 2. `calculate_text_width(text: str, font_size: int, font_name: str = "...")`
Calculates the pixel width of a given text.

#### Parameters
- `text` (str): Text to measure
- `font_size` (int): Size of the font
- `font_name` (str, optional): Path to font file

#### Returns
- Text width in pixels
- Fallback to default font if specified font not found

### 3. `split_text_to_width(text: str, max_width: float, font_size: int, font_name: str = "IBM Plex Sans")`
Splits text into lines that fit within a specified width.

#### Parameters
- `text` (str): Input text
- `max_width` (float): Maximum line width
- `font_size` (int): Font size
- `font_name` (str, optional): Font name

#### Returns
- List of text lines
- Each line fits within `max_width`

#### Algorithm
- Dynamically splits text based on word widths
- Preserves word integrity
- Handles multi-line text wrapping

### 4. `computeLineSpacing(fontSize: float, lineHeightMultiplier: float, lineSpacingMultiplier: float)`
Calculates line spacing for text rendering.

#### Parameters
- `fontSize` (float): Base font size
- `lineHeightMultiplier` (float): Line height adjustment factor
- `lineSpacingMultiplier` (float): Additional spacing multiplier

#### Returns
- Computed line spacing value

### 5. `calculate_scaling_factor(font_size: int, desired_height: float, font_path: str = "...")`
Computes scaling factor to match desired text height.

#### Parameters
- `font_size` (int): Initial font size
- `desired_height` (float): Target text height
- `font_path` (str, optional): Path to font file

#### Returns
- Scaling factor to achieve desired height

## Dependencies
- `yaml`: YAML configuration parsing
- `PIL.ImageFont`: Font and text measurement

## Default Configurations
- Default Font: IBM Plex Sans
- Default Font Path: `lecturePipeline/typography/fonts/IBM_Plex_Sans/IBMPlexSans-Light.ttf`

## Usage Examples

### Typography Configuration
```python
# Retrieve font size
font_size = typography('heading.size', default=24)

# Retrieve font family
font_family = typography('font.primary', default='IBM Plex Sans')
```

### Text Width Calculation
```python
width = calculate_text_width("Hello, World!", font_size=20)
```

### Text Wrapping
```python
lines = split_text_to_width(
    "This is a long text that needs wrapping", 
    max_width=300, 
    font_size=16
)
```

### Line Spacing
```python
spacing = computeLineSpacing(
    fontSize=20, 
    lineHeightMultiplier=1.5, 
    lineSpacingMultiplier=0.2
)
```

## Error Handling
- Graceful fallback for missing font files
- Default values for configuration retrieval
- Informative error messages

## Best Practices
- Use configuration-driven typography
- Leverage text measurement for precise layout
- Implement consistent text wrapping
- Dynamically adjust text scaling