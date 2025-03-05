# data-science-bangladeshi-student-counts

# Project Overview
This project analyzes the class-wise age distribution of students in Bangladesh from classes six to ten. The pipeline includes data preprocessing, exploratory data analysis (EDA), feature engineering, predictive modeling, and result visualization.

# Folder Structure
```
project-root/
├── data/                 # Contains the raw dataset
│   ├── data_resource_2018_02_05_Student_By_Age.csv
├── scripts/              # Contains Python scripts for each step of the analysis
│   ├── 01_preprocessing.py
│   ├── 02_eda.py
│   ├── 03_feature_engineering.py
│   ├── 04_modeling.py
│   ├── 05_results_visualization.py
├── outputs/              # Stores processed data, model results, and visualizations
├── requirements.txt      # Lists required Python dependencies
├── README.md             # Project documentation
```

# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

## 2. Run the scripts in order:

### Data Preprocessing
```sh
python scripts/01_preprocessing.py
```
Cleans and processes the dataset, saving the cleaned version to `outputs/cleaned_data.csv`.

### Exploratory Data Analysis (EDA)
```sh
python scripts/02_eda.py
```
Generates statistical summaries and visualizations saved in `outputs/`.

### Feature Engineering
```sh
python scripts/03_feature_engineering.py
```
Creates new features and saves the transformed dataset to `outputs/feature_engineered_data.csv`.

### Modeling
```sh
python scripts/04_modeling.py
```
Trains a predictive model and saves performance metrics in `outputs/model_performance.txt`.

### Results Visualization
```sh
python scripts/05_results_visualization.py
```
Generates final visualizations and insights, saving output files in `outputs/`.

# Requirements
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

# Acknowledgments
**Dataset Name:** BangladeshiStudents:Classwise(6-10)AgeDistribution  
**Dataset Author:** Shuvo Kumar Basak-4004.o  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/shuvokumarbasak2030/bangladeshistudentsclasswise6-10agedistribution)