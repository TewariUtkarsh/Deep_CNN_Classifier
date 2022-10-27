import os
import urllib.request as request
from zipfile import ZipFile
from typing import List
from DeepClassifier import logger
from DeepClassifier.entity import DataIngestionConfig
from DeepClassifier.utils import get_file_size
from tqdm import tqdm
from pathlib import Path
import progressbar


class MyProgressBar:
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar = progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        """
        This function downloads data from the url to the desired location.
        """
        logger.info("Attemping to download data files....")
        if not os.path.exists(self.config.downloaded_data_file_path):
            logger.info("Downloading files....")
            filepath, httpmessage = request.urlretrieve(
                self.config.source_download_url,
                self.config.downloaded_data_file_path,
                MyProgressBar(),
            )
            logger.info(f"{filepath} file download successfully. INFO: \n{httpmessage}")

        else:
            logger.info(
                f"File already exists [SIZE: {get_file_size(Path(self.config.downloaded_data_file_path))}]. Skipping Download."
            )

    def _get_updated_list_of_files(self, list_of_files: List) -> List:
        updated_list_of_files = [
            file
            for file in list_of_files
            if file.endswith(".jpg") and ("Cat" in file or "Dog" in file)
        ]
        return updated_list_of_files

    def _preprocess(self, zf: ZipFile, f: str, dir: str):
        target_file_path = os.path.join(dir, f)

        if not os.path.exists(target_file_path):
            zf.extract(f, dir)

        if os.path.getsize(target_file_path) == 0:
            logger.info(f"Removing {target_file_path} file as size is 0 KB.")
            os.remove(target_file_path)

    def unzip_and_clean_data(self):
        """
        This function performs a validity check on the files:
        1. Extract those files which end with .jpg ext.
        2. Remove those extracted files which have a file size of 0.
        """
        logger.info("Attempting to unzip and integrity check for downloaded files")
        with ZipFile(file=self.config.downloaded_data_file_path, mode="r") as file_obj:
            list_of_files = file_obj.namelist()
            updated_list_of_files = self._get_updated_list_of_files(
                list_of_files=list_of_files
            )

            for file in tqdm(updated_list_of_files):
                self._preprocess(file_obj, file, self.config.unzipped_data_dir)

        logger.info("Unzipping and cleaning completed")

    def __del__(self):
        logger.info("Data Ingestion Stage Completed")
