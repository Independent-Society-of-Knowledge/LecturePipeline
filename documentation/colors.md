# Color Management Module Documentation

## Overview
This module provides a structured color management system for the Independent Society of Knowledge (ISK) lecture design, offering predefined color palettes with systematic color gradations.

## Color Palette Classes

### 1. `PrimaryColor` Class
Represents the primary color palette with 10 gradation levels.

#### Color Range
- Level 10: Darkest primary color (`#240B43`)
- Level 1: Lightest primary color (`#F2E2FF`)

#### Methods
- `get(num: int)`: Retrieves color for a specific level

### 2. `DarkColor` Class
Represents the dark color palette with 10 gradation levels.

#### Color Range
- Level 10: Darkest shade (`#606060`)
- Level 1: Absolute black (`#000000`)

#### Methods
- `get(num: int)`: Retrieves color for a specific level

### 3. `LightColor` Class
Represents the light color palette with 10 gradation levels.

#### Color Range
- Level 10: Dark gray (`#717171`)
- Level 1: Pure white (`#FFFFFF`)

#### Methods
- `get(num: int)`: Retrieves color for a specific level

## Utility Function

### `getColor(name: str, num: int)`
A convenience function to retrieve colors from different palettes.

#### Parameters
- `name` (str): Color palette name
  - Options: `"primary"`, `"dark"`, `"light"`
- `num` (int): Color level (1-10)

#### Returns
- `ManimColor`: Selected color
- `"No-Color-Found"`: If invalid palette name

## Usage Examples

```python
# Retrieve primary color at level 5
primary_mid = getColor("primary", 5)

# Retrieve dark color at level 3
dark_shade = getColor("dark", 3)

# Retrieve light color at level 1
white = getColor("light", 1)
```

## Design Principles
- Systematic color gradation
- Consistent naming convention
- Easy programmatic color selection
- Manim-compatible color representation

## Best Practices
- Use levels 1-10 for color selection
- Prefer using `getColor()` for color retrieval
- Maintain color consistency across lectures

## Compatibility
- Works with Manim's `ManimColor` class
- Supports hex color representation

## Error Handling
- Returns `"No-Color-Found"` for invalid palette names
- Supports integer input conversion