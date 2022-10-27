import tensorflow as tf
from pathlib import Path
from DeepClassifier.utils import save_json
from DeepClassifier.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(
            self,
            model_evaluation_config:ModelEvaluationConfig,

        ):
        self.model_evaluation_config = model_evaluation_config

    def _get_valid_generator(self):
        data_generator_kwargs = dict(
            rescale=1/255.,
            validation_split=0.30,
        )

        valid_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        data_flow_kwargs = dict(
            target_size=self.model_evaluation_config.params.IMAGE_SHAPE[:-1],
            batch_size=self.model_evaluation_config.params.BATCH_SIZE,
            interpolation='bilinear'
        )


        self.valid_data_generator =valid_generator.flow_from_directory(
            self.model_evaluation_config.test_data_dir,
            subset='validation',
            shuffle=False,
            **data_flow_kwargs
        )

        
    @staticmethod
    def load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)


    def evaluate(self):
        self._get_valid_generator()
        model = self.load_model(path=Path(self.model_evaluation_config.trained_model_filepath))
        self.scores = model.evaluate(self.valid_data_generator)
        self.save_scores()

    def save_scores(self):
        self.scores = {"loss": self.scores[0], "accuracy": self.scores[1]}
        save_json(path=Path(self.model_evaluation_config.scores_filepath),data=self.scores)
        