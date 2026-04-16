from fastapi import FastAPI
from schemas import InputSchmema, outputSchema
from predict import make_prediction, make_batch_prediction
from typing import List

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'welcome to the house price prediction API'}

@app.post('/predict', response_model=outputSchema)
def predict(user_input: InputSchmema):
    prediction= make_prediction(user_input.model_dump())
    return outputSchema(predicted_price=round(prediction, 2))

@app.post('/batch_predict', response_model=List[outputSchema])
def batch_predict(User_inputs: List[InputSchmema]):
    predictions = make_batch_prediction([x.model_dump() for x in User_inputs])
    return [outputSchema(predicted_price=round(prediction, 2)) for prediction in predictions]
