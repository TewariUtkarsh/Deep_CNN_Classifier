from DeepClassifier.config import ConfigurationManager
from DeepClassifier.components import DataIngestion
from DeepClassifier import logger


STAGE_NAME = "Data Ingestion Stage"


def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.unzip_and_clean_data()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nx{1000*'='}x")
    except Exception as e:
        logger.exception(e)
        raise e
