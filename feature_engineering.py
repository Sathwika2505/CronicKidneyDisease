from data_preprocessing import data_preprocess
from sklearn.preprocessing import LabelEncoder

def feature_engineering():
    data = data_preprocess()
    cols = ['Pus cells','Hypertension','DiabetesMellitus','Appetite','Anemia','Target']
    labelencoder = LabelEncoder()
    for column in cols:
        data[column] = labelencoder.fit_transform(data[column])
    print(data)

    df=data.drop(["Redbloodcellscount","Whitebloodcellscount"],axis=1)

    df.to_csv('kidney_disease_artifact.csv', index=False)

    print(df.dtypes)

    return data
feature_engineering()
