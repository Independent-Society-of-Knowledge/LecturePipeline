import yaml
import yaml
from typing import Any, Optional

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

if __name__ == "__main__":
    print(typography("fluid.display-01-mx"))
