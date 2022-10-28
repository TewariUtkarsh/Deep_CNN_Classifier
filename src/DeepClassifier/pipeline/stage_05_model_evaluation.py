from DeepClassifier.config import ConfigurationManager
from DeepClassifier.components import ModelEvaluation
from DeepClassifier import logger


STAGE_NAME = "Model Evaluation Stage"


def main():
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evaluation_config()
    model_evaluation = ModelEvaluation(model_evaluation_config)
    model_evaluation.evaluate()

if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nx{1000*'='}x")
    except Exception as e:
        logger.exception(e)
        raise e
