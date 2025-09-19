from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.model_trainer import ModelTrainer
from src.textSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()