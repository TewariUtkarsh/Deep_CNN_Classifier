import tensorflow as tf
from DeepClassifier.entity import PrepareBaseModelConfig
from pathlib import Path


class PrepareBaseModel:
    def __init__(self, config=PrepareBaseModelConfig) -> None:
        self.config = config

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def get_base_model(self):
        self.base_model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params.IMAGE_SHAPE,
            include_top=self.config.params.INCLUDE_TOP,
            weights=self.config.params.WEIGHTS)

        base_model_path = self.config.base_model_path

        self.save_model(base_model_path, self.base_model)

    @staticmethod
    def _prepare_full_model(
        base_model, classes, freeze_all, freeze_till, learning_rate
    ) -> tf.keras.models.Model:
        if freeze_all:
            for layer in base_model.layers:
                layer.trainable = False

        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in base_model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_layer = tf.keras.layers.Flatten()(base_model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(
            flatten_layer
        )

        full_model = tf.keras.models.Model(inputs=base_model.input, outputs=prediction)

        full_model.compile(
            loss=tf.keras.losses.CategoricalCrossentropy(),
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            metrics=["accuracy"],
        )

        return full_model

    def update_base_model(self):
        self.final_model = self._prepare_full_model(
            base_model=self.base_model,
            classes=self.config.params.CLASSES,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params.LEARNING_RATE,
        )

        self.save_model(self.config.updated_base_model_path, self.final_model)
