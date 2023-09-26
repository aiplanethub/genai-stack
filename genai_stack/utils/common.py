from pathlib import Path
import json


def load_json(json_file_path: str):
    f = Path(json_file_path)

    if not f.exists():
        raise ValueError(
            f"Unable to find the file. Input given - {json_file_path}",
        )

    try:
        with open(f.absolute()) as file:
            data = json.load(file)
            return data

    except json.JSONDecodeError as e:
        raise ValueError("Unable to read the json file.") from e
