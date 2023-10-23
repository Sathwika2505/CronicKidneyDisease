from data_preprocessing import data_preprocess
from sklearn.preprocessing import LabelEncoder

def feature_engineering():
    data = data_preprocess()
    cols = ['Pus cells','Hypertension','DiabetesMellitus','Appetite','Anemia','Target']
    labelencoder = LabelEncoder()
    for column in cols:
        data[column] = labelencoder.fit_transform(data[column])
    print(data)

    data.to_csv('kidney_disease_artifact.csv', index=False)

    return data
feature_engineering()
