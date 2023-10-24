import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engineering import feature_engineering

def data_visualization():
    dataset = feature_engineering()
    categ = ['Target']
    numer = ['Age(yrs)', 'Blood Pressure', 'Specific Grafity', 'Albumin','Blood Urea', 'Serum Creatinine', 'Sodium', 
             'Potassium', 'Haemoglobin','Whitebloodcellscount', 'Redbloodcellscount', 'Hypertension', 
             'DiabetesMellitus']
    # column_name = 'YourColumnNameHere'
    plt.figure(figsize=(10,8))
    sns.heatmap(dataset.drop('Target').corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()
    
    for x in numer:
        # Ensure the column is numeric and replace non-numeric values with NaN
        dataset[x] = pd.to_numeric(dataset[x], errors='coerce')
        q75, q25 = np.percentile(dataset.loc[:, x].dropna(), [75, 25])
        intr_qr = q75 - q25
        max_val = q75 + (1.5 * intr_qr)
        min_val = q25 - (1.5 * intr_qr)
        dataset.loc[dataset[x] < min_val, x] = np.nan
        dataset.loc[dataset[x] > max_val, x] = np.nan
    # Box plots
    for num in numer:
        plt.figure(figsize=(5, 5))
        sns.boxplot(data=dataset, x=num)
        plt.xlabel(num)
    plt.show()
    for numeric in numer:
        plt.subplots(1,1, figsize=(5,5))
        sns.distplot(x = dataset[numeric])
        plt.xlabel(numeric)
        plt.title(numeric)
    plt.show()
    return dataset

data_visualization()
