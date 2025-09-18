from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str


@dataclass
class DataTransformationConfig:
    root_dir: str
    data_path: str
    tokenizer_name: str
    max_input_length: int
    max_target_length: int
