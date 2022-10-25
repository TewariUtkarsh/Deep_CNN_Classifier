from pathlib import Path
from DeepClassifier.constants import CONFIG_FILEPATH, PARAMS_FILEPATH
from DeepClassifier.utils import read_yaml_file, make_directories
from DeepClassifier.entity import (
    DataIngestionConfig,
    PrepareBaseModelConfig,
    PrepareCallbacksConfig,
    ModelTrainingConfig,
    ModelEvaluationConfig
)
import os


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILEPATH,
        params_filepath: Path = PARAMS_FILEPATH,
    ) -> None:
        self.config = read_yaml_file(filepath=config_filepath)
        self.params = read_yaml_file(filepath=params_filepath)

        dir_to_be_created = [
            self.config.root_artifact_dir,
        ]
        make_directories(dir_to_be_created)

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        data_ingestion_config_info = self.config.data_ingestion

        make_directories([data_ingestion_config_info.artifact_dir])

        data_ingestion_config = DataIngestionConfig(
            artifact_dir=data_ingestion_config_info.artifact_dir,
            source_download_url=data_ingestion_config_info.source_download_url,
            downloaded_data_file_path=data_ingestion_config_info.downloaded_data_file_path,
            unzipped_data_dir=data_ingestion_config_info.unzipped_data_dir,
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        prepare_base_model_config_info = self.config.prepare_base_model

        artifact_dir = prepare_base_model_config_info.artifact_dir

        make_directories([artifact_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            artifact_dir=Path(artifact_dir),
            params=self.params,
            base_model_path=Path(prepare_base_model_config_info.base_model_path),
            updated_base_model_path=Path(
                prepare_base_model_config_info.updated_base_model_path
            ),
        )

        return prepare_base_model_config

    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        prepare_callbacks_config_info = self.config.prepare_callbacks

        make_directories(
            [
                Path(prepare_callbacks_config_info.artifact_dir),
                Path(prepare_callbacks_config_info.tensorboard_log_dir),
                Path(
                    os.path.dirname(
                        prepare_callbacks_config_info.checkpoint_model_filepath
                    )
                ),
            ]
        )

        prepare_callbacks_config = PrepareCallbacksConfig(
            artifact_dir=Path(prepare_callbacks_config_info.artifact_dir),
            tensorboard_log_dir=Path(prepare_callbacks_config_info.tensorboard_log_dir),
            checkpoint_model_filepath=Path(
                prepare_callbacks_config_info.checkpoint_model_filepath
            ),
        )

        return prepare_callbacks_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        model_training_config_info = self.config.model_training

        make_directories(
            [
                Path(model_training_config_info.artifact_dir),
            ]
        )

        training_data_dir = os.path.join(
            self.config.data_ingestion.unzipped_data_dir, "PetImages"
        )
        model_training_config = ModelTrainingConfig(
            artifact_dir=Path(model_training_config_info.artifact_dir),
            trained_model_filepath=Path(
                model_training_config_info.trained_model_filepath
            ),
            updated_base_model_path=Path(
                self.config.prepare_base_model.updated_base_model_path
            ),
            params=self.params,
            training_data_dir=Path(training_data_dir),
        )

        return model_training_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        model_evaluation_config_info = self.config.model_evaluation

        model_evaluation_config = ModelEvaluationConfig(
            trained_model_filepath=self.config.model_training.trained_model_filepath,
            test_data_dir=self.config.data_ingestion.unzipped_data_dir,
            params=self.params,
            scores_filepath=model_evaluation_config_info.scores_filepath,
            remote_server_uri=model_evaluation_config_info.remote_server_uri
        )

        return model_evaluation_config