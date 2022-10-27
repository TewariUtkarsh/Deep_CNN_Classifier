import tensorflow as tf
from DeepClassifier.entity import ModelTrainingConfig
from pathlib import Path


class ModelTraining:
    def __init__(
        self,
        model_training_config: ModelTrainingConfig,
    ):
        self.model_training_config = model_training_config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.model_training_config.updated_base_model_path)

    def get_train_valid_generator(self):
        data_generator_kwargs = dict(
            rescale=1 / 255.0,
            validation_split=0.20,
        )

        valid_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        data_flow_kwargs = dict(
            target_size=self.model_training_config.params.IMAGE_SHAPE[:-1],
            batch_size=self.model_training_config.params.BATCH_SIZE,
            interpolation="bilinear",
        )

        self.valid_data_generator = valid_generator.flow_from_directory(
            self.model_training_config.training_data_dir,
            subset="validation",
            shuffle=False,
            **data_flow_kwargs)

        if self.model_training_config.params.AUGMENTATION:
            train_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_generator_kwargs
            )
        else:
            train_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                **data_generator_kwargs
            )

        self.train_data_generator = train_generator.flow_from_directory(
            self.model_training_config.training_data_dir,
            subset="training",
            shuffle=True,
            **data_flow_kwargs)

    @staticmethod
    def save_model(path: Path, model: tf.keras.models.Model) -> None:
        model.save(path)

    def train(self, callbacks: list):
        self.steps_per_epoch = (self.train_data_generator.samples // self.train_data_generator.batch_size)
        self.validation_steps = (self.valid_data_generator.samples // self.valid_data_generator.batch_size)

        self.model.fit(
            self.train_data_generator,
            epochs=self.model_training_config.params.EPOCHS,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_data_generator,
            callbacks=callbacks)

        self.save_model(path=self.model_training_config.trained_model_filepath, model=self.model)
