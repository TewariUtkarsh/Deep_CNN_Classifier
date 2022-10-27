from DeepClassifier.entity import PrepareCallbacksConfig
import tensorflow as tf
import time
import os


class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig) -> None:
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        log_dir = os.path.join(self.config.tensorboard_log_dir, f"tb_logs_at_{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir=log_dir)

    @property
    def _create_ckpt_callbacks(self):
        # timestamp = time.strftime("")
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True,
            mode="auto",
        )

    @property
    def _create_early_stopping_callbacks(self):
        return tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", mode="auto", patience=10, restore_best_weights=True
        )

    def get_callbacks(self) -> list:
        callbacks = [self._create_tb_callbacks, self._create_ckpt_callbacks]

        return callbacks
