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

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int