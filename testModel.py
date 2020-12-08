import pandas as pd
import numpy as np
import pickle    
    

dataset = pd.read_csv('heart_failure_clinical_records_dataset.csv')

Datos = ['age','sex','creatinine_phosphokinase','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','time']
x = dataset[Datos]
y = dataset['DEATH_EVENT']
print(x.iloc[0].values,y.iloc[0])

# load the model from disk
loaded_model = pickle.load(open("modeloIC.sav", 'rb'))
result = loaded_model.predict(x.iloc[0].values.reshape(1,8))
print(result) 
