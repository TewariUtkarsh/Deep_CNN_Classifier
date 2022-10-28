from DeepClassifier.config import ConfigurationManager
from DeepClassifier.components import PrepareBaseModel
from DeepClassifier import logger


STAGE_NAME = "Prepare Base Model Stage"


def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nx{1000*'='}x")
    except Exception as e:
        logger.exception(e)
        raise e
