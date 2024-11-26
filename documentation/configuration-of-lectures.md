# LectureConfiguration Class Documentation

## Overview
The `LectureConfiguration` class provides a robust and flexible mechanism for loading and accessing configuration data from YAML files, specifically designed for lecture-based configurations.

## Class Signature
```python
class LectureConfiguration:
    def __init__(self, file_path: str)
```

## Methods

### 1. `__init__(file_path: str)`
Initializes the lecture configuration by loading a YAML file.

#### Parameters
- `file_path` (str): Path to the YAML configuration file

#### Behavior
- Stores the file path
- Calls `_load_yaml()` to parse the configuration
- Stores parsed configuration in `self.data`

### 2. `_load_yaml() -> dict`
Private method to load and parse the YAML configuration file.

#### Returns
- Dictionary representation of the YAML content

#### Exceptions
- Raises `FileNotFoundError` if the file cannot be found
- Raises `ValueError` for YAML parsing errors

### 3. `get(key: str, default: Any = None) -> Any`
Retrieves configuration values using dot-notation path access.

#### Parameters
- `key` (str): Dot-separated key path (e.g., 'lecture.metadata.title')
- `default` (Any, optional): Value to return if key is not found

#### Returns
- Value associated with the key
- Default value if key is not found

#### Example
```python
config = LectureConfiguration('lecture.yaml')
title = config.get('lecture.metadata.title', 'Untitled')
```

### 4. `getMetadata() -> Optional[dict]`
Retrieves lecture metadata.

#### Returns
- Metadata dictionary
- `None` if metadata is not found

### 5. `getSceneConfiguration() -> Optional[dict]`
Retrieves scene configurations.

#### Returns
- Scene configurations dictionary
- `None` if scene configurations are not found

### 6. `getDictionary() -> dict`
Retrieves the complete configuration dictionary.

#### Returns
- Full parsed dictionary from the YAML file

## Usage Example
```python
# Load configuration
config = LectureConfiguration('lecture_config.yaml')

# Access metadata
metadata = config.getMetadata()

# Get specific configuration value
lecture_title = config.get('lecture.metadata.title')

# Retrieve full configuration
full_config = config.getDictionary()
```

## Key Features
- Dot-notation configuration access
- Graceful handling of missing keys
- Robust YAML parsing
- Typed configuration retrieval
- Optional default values

## Best Practices
- Use absolute or relative paths to YAML files
- Ensure YAML files are well-structured
- Provide default values for critical configuration parameters
- Handle potential `FileNotFoundError` and parsing exceptions

## Error Handling
- Raises `FileNotFoundError` for missing configuration files
- Raises `ValueError` for YAML parsing issues
- Returns `None` or default value for missing configuration keys