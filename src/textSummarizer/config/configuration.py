# import sys
# from pathlib import Path

# # Add project root to Python path
# sys.path.append(str(Path(__file__).resolve().parents[3]))

# from src.textSummarizer.constants import *
# from src.textSummarizer.utils.common import read_yaml, create_directories
# from src.textSummarizer.entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig

# class ConfigurationManager:
#     def __init__(self, config_path=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
#         # Convert to Path objects (fixes EnsureError)
#         config_path = Path(config_path)
#         params_filepath = Path(params_filepath)

#         # Load YAML files
#         self.config = read_yaml(config_path)
#         self.params = read_yaml(params_filepath)
        
#         # Ensure artifacts root exists
#         create_directories([Path(self.config.artifacts_root)])

#     def get_data_ingestion_config(self) -> DataIngestionConfig:
#         config = self.config.data_ingestion
#         create_directories([Path(config.root_dir)])

#         return DataIngestionConfig(
#             root_dir=Path(config.root_dir),
#             source_URL=config.source_URL,
#             local_data_file=Path(config.local_data_file),
#             unzip_dir=Path(config.unzip_dir)
#         )

#     def get_data_transformation_config(self) -> DataTransformationConfig:
#         config = self.config.data_transformation
#         create_directories([Path(config.root_dir)])

#         return DataTransformationConfig(
#             root_dir=Path(config.root_dir),
#             data_path=Path(config.data_path),
#             tokenizer_name=config.tokenizer_name,
#             max_input_length=self.params.DataTransformation.max_input_length,
#             max_target_length=self.params.DataTransformation.max_target_length
#         )
#     def get_model_trainer_config(self) -> ModelTrainerConfig:
#         config = self.config.model_trainer
#         params = self.params.TrainingArguments
        
#         create_directories([config.root_dir])
        
#         return ModelTrainerConfig(
#             root_dir=config.root_dir,
#             data_path=config.data_path,
#             model_ckpt=config.model_ckpt,
#             num_train_epochs=params.num_train_epoches,
#             warmup_steps=params.warmup_steps,
#             per_device_train_batch_size=params.per_device_train_batch_size,
#             weight_decay=params.weight_decay,
#             logging_steps=params.logging_steps,
#             evaluation_strategy=params.evaluation_strategy,
#             eval_steps=params.eval_steps,
#             save_steps=params.save_steps,
#             gradient_accumulation_steps=params.gradient_accumulation_steps
#         )

import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[3]))

from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
# from src.textSummarizer.entity import DataIngestionConfig, DataTransformationConfig
# from src.textSummarizer.entity import ModelTrainerConfig
from src.textSummarizer.entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)



class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        # Convert to Path objects (fixes EnsureError)
        config_path = Path(config_path)
        params_filepath = Path(params_filepath)

        # Load YAML files
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_filepath)
        
        # Ensure artifacts root exists
        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([Path(config.root_dir)])

        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([Path(config.root_dir)])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            tokenizer_name=config.tokenizer_name,
            max_input_length=self.params.DataTransformation.max_input_length,
            max_target_length=self.params.DataTransformation.max_target_length
        )

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments
        
        create_directories([Path(config.root_dir)])
        
        return ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,  # Make sure YAML key matches
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
