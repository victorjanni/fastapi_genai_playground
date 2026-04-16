import joblib
import numpy as np


saved_model = joblib.load('model.joblib')
print('model loaded')

def make_prediction(data: dict) -> float:
    feautures = np.array([[
        data['Longitude'],
        data['latitude'],   
        data['housing_median_age'],
        data['total_rooms'],           
        data['total_bedrooms'],
        data['population'],
        data['households'],
        data['median_income']
    ]])

    return saved_model.predict(feautures)[0]