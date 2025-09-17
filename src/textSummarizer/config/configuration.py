# # src/textSummarizer/configuration.py

# import os
# from pathlib import Path
# from src.textSummarizer.utils.common import read_yaml, create_directories

# # Optional: add src to sys.path if needed (mainly for notebooks)
# import sys
# sys.path.append(os.path.join(os.getcwd(), "src"))

# class ConfigurationManager:
#     """
#     This class reads configuration files (YAML) and provides
#     easy access to config and parameter values.
#     """

#     def __init__(self, config_path: str = None, params_filepath: str = None):
#         """
#         Initializes ConfigurationManager with paths to config and params files.
#         If paths are not provided, defaults to 'config.yaml' and 'params.yaml' in the project root.

#         Args:
#             config_path (str, optional): Path to the config.yaml file.
#             params_filepath (str, optional): Path to params.yaml file.
#         """
#         if config_path is None:
#             config_path = "config.yaml"
#         if params_filepath is None:
#             params_filepath = "params.yaml"

#         self.config = read_yaml(Path(config_path))
#         self.params = read_yaml(Path(params_filepath))

#         # Ensure artifacts root exists
#         create_directories([self.config.artifacts_root])

#     def get_data_ingestion_config(self):
#         """
#         Returns data ingestion related configuration as a dictionary.
#         """
#         return self.config.data_ingestion

#     def get_artifacts_root(self):
#         """
#         Returns the root directory for storing artifacts.
#         """
#         return self.config.artifacts_root

# from src.textSummarizer.constants import *
from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH,
                params_filepath=PARAMS_FILE_PATH):
        self.config=read_yaml(config_path)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
