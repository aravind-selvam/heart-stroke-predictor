import os
import sys
from six.moves import urllib
import pandas as pd
from heart_stroke.constant import *
from heart_stroke.logger import logging
from heart_stroke.entity.config_entity import DataIngestionConfig
from heart_stroke.entity.artifact_entity import DataIngestionArtifact
from heart_stroke.config.configuration import Configuartion
from heart_stroke.exception import HeartStrokeException
from heart_stroke.utils.util import read_yaml_file
from sklearn.model_selection import train_test_split


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>'*30}Data Ingestion log started.{'<<'*30} \n\n")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HeartStrokeException(e, sys) from e

    def download_data(self) -> str:
        try:
            download_url = self.data_ingestion_config.dataset_download_url

            raw_data_dir = self.data_ingestion_config.raw_data_dir

            os.makedirs(raw_data_dir, exist_ok=True)

            heart_stroke_file_name = os.path.basename(download_url)

            raw_file_path = os.path.join(raw_data_dir, heart_stroke_file_name)

            logging.info(
                f"Downloading file from :[{download_url}] into :[{raw_file_path}]")
            urllib.request.urlretrieve(download_url, raw_file_path)
            logging.info(
                f"File :[{raw_file_path}] has been downloaded successfully.")
            return raw_file_path

        except Exception as e:
            raise HeartStrokeException(e, sys) from e
        
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            file_name = os.listdir(raw_data_dir)[0]

            heart_stroke_file_path = os.path.join(raw_data_dir, file_name)

            logging.info(f"Reading csv file: [{heart_stroke_file_path}]")
            heart_stroke_dataframe = pd.read_csv(heart_stroke_file_path)
            heart_stroke_dataframe.drop('id', axis=1, inplace=True)
            
            logging.info(f"Splitting data into train and test")

            train_set = None
            test_set = None

            train_set, test_set = train_test_split(heart_stroke_dataframe, test_size=0.2, random_state=42)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                           file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                          file_name)

            if train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(f"Exporting training dataset to file: [{train_file_path}]")
                train_set.to_csv(train_file_path, index=False)

            if test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                test_set.to_csv(test_file_path, index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                                            test_file_path=test_file_path,
                                                            is_ingested=True,
                                                            message=f"Data ingestion completed successfully."
                                                            )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise HeartStrokeException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            raw_file_path = self.download_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise HeartStrokeException(e, sys)from e