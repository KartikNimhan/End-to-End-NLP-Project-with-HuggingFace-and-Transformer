import os
from src.textSummarizer.logging import logger
from datasets import load_dataset, load_from_disk  # ✅ Added load_dataset
from transformers import AutoTokenizer


class DataTransformationConfig:
    """
    Configuration class to store parameters for data transformation.
    """
    def __init__(self):
        # Tokenizer and dataset paths
        self.tokenizer_name = "google/pegasus-cnn_dailymail"
        self.data_path = "artifacts/data_ingestion/samsum_dataset"
        self.root_dir = "artifacts/data_transformation"

        # Tokenization settings
        self.max_input_length = 512     # maximum length for input dialogue
        self.max_target_length = 128    # maximum length for summary


class DataTransformation:
    """
    Handles tokenization and preprocessing of the SAMSum dataset for model training.
    """
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        """
        Convert a batch of examples (dialogue + summary) into tokenized input_ids, attention_mask, and labels.
        """
        input_encodings = self.tokenizer(
            example_batch['dialogue'],
            max_length=self.config.max_input_length,
            padding='max_length',
            truncation=True
        )

        target_encodings = self.tokenizer(
            example_batch['summary'],
            max_length=self.config.max_target_length,
            padding='max_length',
            truncation=True
        )

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert_dataset(self):  # ✅ Renamed to match pipeline
        """
        Loads the dataset (downloading if necessary), tokenizes it, and saves it to disk.
        """
        # If dataset directory does not exist, download SAMSum
        if not os.path.exists(self.config.data_path):
            logger.info(f"Dataset not found at {self.config.data_path}. Downloading SAMSum dataset...")
            dataset_samsum = load_dataset("samsum")
            os.makedirs(self.config.data_path, exist_ok=True)
            dataset_samsum.save_to_disk(self.config.data_path)
            logger.info("Dataset downloaded and saved locally.")

        # Load dataset from disk
        dataset_samsum = load_from_disk(self.config.data_path)

        # Tokenize dataset
        logger.info("Tokenizing dataset... this may take a few minutes.")
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)

        # Save processed dataset
        save_path = os.path.join(self.config.root_dir, "samsum_dataset")
        os.makedirs(self.config.root_dir, exist_ok=True)
        dataset_samsum_pt.save_to_disk(save_path)
        logger.info(f"Tokenized dataset saved successfully at {save_path}")



# ------------------------------
# Script entry point (for standalone testing)
# ------------------------------
if __name__ == "__main__":
    config = DataTransformationConfig()
    transformer = DataTransformation(config=config)
    transformer.convert_dataset()  # ✅ Updated to use new method name
