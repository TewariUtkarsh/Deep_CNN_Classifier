from dataclasses import dataclass
from pathlib import Path
from box import ConfigBox


# Data Ingestion Configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    artifact_dir: Path
    source_download_url: str
    downloaded_data_file_path: Path
    unzipped_data_dir: Path


# Prepare Base Model Configuration
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    artifact_dir: Path
    params: ConfigBox
    base_model_path: Path
    updated_base_model_path: Path


# Prepare Callbacks Configuration
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    artifact_dir: Path
    tensorboard_log_dir: Path
    checkpoint_model_filepath: Path


# Model Training Configuration
@dataclass(frozen=True)
class ModelTrainingConfig:
    artifact_dir: Path
    trained_model_filepath: Path
    updated_base_model_path: Path
    training_data_dir: Path
    params: ConfigBox


# Model Evaluation Configuration
@dataclass(frozen=True)
class ModelEvaluationConfig:
    trained_model_filepath: Path
    test_data_dir: Path
    params: ConfigBox
    scores_filepath: Path
    remote_server_uri: str