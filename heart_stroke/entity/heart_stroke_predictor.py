import os
import sys

from heart_stroke.exception import HeartStrokeException
from heart_stroke.utils.util import load_object

import pandas as pd


class HeartStrokeData:

    def __init__(self, gender: str,
                age : int,
                hypertension : int,
                heart_disease: int,
                ever_married: str,
                work_type : str,
                Residence_type : str,
                avg_glucose_level : float,
                bmi : float,
                smoking_status : str,
                stroke : int = None 
                ):
        try:
            self.gender = gender
            self.age = age
            self.hypertension = hypertension
            self.heart_disease = heart_disease
            self.ever_married = ever_married
            self.work_type = work_type
            self.Residence_type = Residence_type
            self.avg_glucose_level = avg_glucose_level
            self.bmi = bmi
            self.smoking_status = smoking_status

        except Exception as e:
            raise HeartStrokeException(e, sys) from e

    def get_heart_stroke_input_data_frame(self):

        try:
            heart_stroke_input_dict = self.get_heart_stroke_data_as_dict()
            return pd.DataFrame(heart_stroke_input_dict)
        except Exception as e:
            raise HeartStrokeException(e, sys) from e

    def get_heart_stroke_data_as_dict(self):
        try:
            input_data = {
                "gender": [self.gender],
                "age": [self.age],
                "hypertension": [self.hypertension],
                "heart_disease": [self.heart_disease],
                "ever_married": [self.ever_married],
                "work_type": [self.work_type],
                "Residence_type": [self.Residence_type],
                "avg_glucose_level": [self.avg_glucose_level],
                "bmi": [self.bmi],
                "smoking_status": [self.smoking_status]
                }
            return input_data
        except Exception as e:
            raise HeartStrokeException(e, sys)


class predictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise HeartStrokeException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise HeartStrokeException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            predited_value = model.predict(X)
            return predited_value
        except Exception as e:
            raise HeartStrokeException(e, sys) from e
        
    def proba_predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            probaility = model.predict_proba(X)
            return probaility 
        except Exception as e:
            raise HeartStrokeException(e, sys) from e
