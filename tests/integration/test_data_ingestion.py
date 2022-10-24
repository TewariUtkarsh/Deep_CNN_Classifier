import pytest, os, glob
from DeepClassifier.entity import DataIngestionConfig
from DeepClassifier.components import DataIngestion
from pathlib import Path

class Test_DataIngestion:
    artifact_dir = Path('tests/data/')
    source_download_url = 'https://raw.githubusercontent.com/TewariUtkarsh/Deep_CNN_Classifier/master/sample_data.zip'
    downloaded_data_filepath = Path('tests/data/integration.zip')
    unzipped_data_dir = Path('tests/data/')

    data_ingestion_config = DataIngestionConfig(
                                artifact_dir=artifact_dir,
                                source_download_url=source_download_url,
                                downloaded_data_file_path=downloaded_data_filepath,
                                unzipped_data_dir=unzipped_data_dir
                            )

    
    def test_download_data(self):
        data_ingestion = DataIngestion(self.data_ingestion_config)
        data_ingestion.download_data()

        assert os.path.exists(self.downloaded_data_filepath)

        
    def test_unzip_and_clean_data(self):
        data_ingestion = DataIngestion(self.data_ingestion_config)
        data_ingestion.unzip_and_clean_data()

        assert os.path.isdir(Path("tests/data/PetImages"))
        assert os.path.isdir(Path("tests/data/PetImages/Cat"))
        assert os.path.isdir(Path("tests/data/PetImages/Dog"))
        


