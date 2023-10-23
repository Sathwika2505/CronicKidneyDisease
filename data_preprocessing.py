from data_loading import loading_data

def data_preprocess():
    data = loading_data()
    data =  data.drop('id', axis = 1)
    columns = ['Age(yrs)', 'Blood Pressure', 'Specific Grafity', 'Albumin', 'Sugar', 'RedBloodCells', 'Pus cells', 'Pus cells cumps', 'Bacteria', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Haemoglobin', 'Packed cell volume', 'Whitebloodcellscount', 'Redbloodcellscount', 'Hypertension', 'DiabetesMellitus', 'Coronary Artery Disease', 'Appetite', 'Pedal Edema', 'Anemia','Target']
    data.columns = columns
    data = data.drop(['Pus cells cumps', 'Bacteria','RedBloodCells','Blood Glucose Random','Packed cell volume','Coronary Artery Disease','Pedal Edema'], axis = 1)
    categorical_data = ['Hypertension','DiabetesMellitus','Appetite','Anemia','Target','Pus cells']
    numerical_data = ['Age(yrs)','Blood Pressure','Whitebloodcellscount','Redbloodcellscount', 'Specific Grafity', 'Albumin', 'Sugar','Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Haemoglobin']
    for cdata in categorical_data:
        data[cdata] = data[cdata].fillna('unknown')
        # print(f"for {data[cdata]} the unique values are : ", data[cdata].unique())
    for ndata in numerical_data:
        data[ndata] = data[ndata].fillna(0)
        # print(f"for {data[ndata]} the unique values are : ", data[ndata].unique())   
    
    # data = data.fillna(0)
    cols = ['Age(yrs)','Blood Pressure','Albumin','Sugar','Blood Urea','Sodium']
    for column in cols:
        data[column] = data[column].astype('int')
        
    # print(data.info())
    return data

data_preprocess()