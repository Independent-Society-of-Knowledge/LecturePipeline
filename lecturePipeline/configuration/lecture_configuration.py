import yaml
from typing import Any, Optional


class LectureConfiguration:
    def __init__(self, file_path: str):
        """
        Initialize CourseConfig with the path to the YAML file.

        :param file_path: Path to the YAML configuration file.
        """
        self.file_path = file_path
        self.data = self._load_yaml()

    def _load_yaml(self) -> dict:
        """
        Load the YAML file and convert it into a Python dictionary.

        :return: A dictionary representation of the YAML content.
        :raises FileNotFoundError: If the file cannot be found.
        :raises yaml.YAMLError: If there's an error parsing the YAML.
        """
        try:
            with open(self.file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from the configuration using dot notation.

        :param key: Dot-separated key path (e.g., 'lecture.metadata.title')
        :param default: Default value to return if key is not found
        :return: Value associated with the key or default
        """
        keys = key.split('.')
        value = self.data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

            if value is None:
                return default

        return value

    def getMetadata(self) -> Optional[dict]:
        """
        Retrieve the lecture metadata.

        :return: Metadata dictionary or None
        """
        return self.get('lecture.metadata')

    def getSceneConfiguration(self) -> Optional[dict]:
        """
        Retrieve scene configurations.

        :return: Scene configurations dictionary or None
        """
        return self.get('lecture.scene-configurations')

    def getDictionary(self) -> dict:
        """
        Get the full dictionary representation of the YAML file.

        :return: The parsed dictionary.
        """
        return self.data
    
