from DeepClassifier.config import ConfigurationManager
from DeepClassifier.components import PrepareCallbacks, ModelTraining
from DeepClassifier import logger


STAGE_NAME = "Model Training Stage"


def main():
    config = ConfigurationManager()

    prepare_callbacks_config = config.get_prepare_callbacks_config()
    prepare_callbacks = PrepareCallbacks(prepare_callbacks_config)
    callbacks = prepare_callbacks.get_callbacks()

    model_training_config = config.get_model_training_config()
    model_training = ModelTraining(
        model_training_config,
    )

    model_training.get_base_model()
    model_training.get_train_valid_generator()
    model_training.train(callbacks=callbacks)


if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nx{1000*'='}x")
    except Exception as e:
        logger.exception(e)
        raise e
