# Heart Stroke Predictor

#### Language and Libraries

<p>
<a><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="Seaborn"/></a>
<a><img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Seaborn"/></a>
<a><img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy"/></a>
 <a><img src="https://matplotlib.org/_static/logo2_compressed.svg" alt="cplusplus" width="110"/></a>
<a><img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn"width="110"/></a>
</p>


## Data
The dataset is collected from the following link: 
https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

* This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status.

## Data Understanding
The dataset used to predict stroke is a dataset from Kaggle. This dataset has been used to predict stroke with 566 different model algorithms. This dataset has:
- 5110 samples or rows
- 11 features or columns 
- 1 target column (stroke).



## Features in Datasets:
1. id : a unique identifier that distinguishes each data [int]
2. Gender: Patient's gender ('Male', 'Female', and 'Other') [str]
3. age : Age of the patient [int]
4. Hypertension: Hypertension or high blood pressure is a disease that puts a person at risk for stroke. 0 if the patient does not have hypertension, 1 if the patient has hypertension. [int]
5. heart_disease: Heart disease is a disease that puts a person at risk for stroke. 0 if the patient does not have heart disease, 1 if the patient has heart disease. [int]
6. ever_married : Describes whether the patient is married or not ('Yes' or 'No') [str]
7. work_type : Type of employment or status ('children' for children, 'Govt_job' for civil servants, 'Never_worked' for those who have never worked, 'Private' or 'Self-employed' for entrepreneurs or freelancers) [str]
8. Residence_type : Condition of residence ('Rural' for rural areas and 'Urban' for urban areas) [str]
9. avg_glucose_level : Average amount of glucose (sugar) in the blood [float]
10. bmi : Body Mass Index to measure the stability of body weight with height. [float]
11. smoking_status : Description of smoking ('formerly smoked' for those who have smoked, 'never smoked' for those who have never smoked, 'smokes' for those who smoke, and 'unknown' for those whose smoking status is unknown) [str]

Target:
stroke : Prediction target if the patient has a stroke then 1, otherwise 0 [int]

## Type of Machine Learning task : 
It is an classification problem where given a set of features we need to predict whether that person is prone to heart diseases or not.

## Performace Metric
Since it is an classification problem we will use AUC-ROC, F1-score, Accuracy, Precision, Recall, and Confusion Matrix.



