from data_loading import loading_data

def data_analysis():

    data = loading_data()
    # print(data.info())
    # print(data.describe())
    # print(data.columns)
    # print(data.shape)
    # print(data.head())
    # print(data.tail())
    # print(data.isnull().sum())
    for col in data.columns:
        print(col, data[col].nunique())

    return data

data_analysis()