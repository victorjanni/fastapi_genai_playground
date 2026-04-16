from fastapi import FastAPI
from schemas import InputSchmema, outputSchema
from predict import make_prediction

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'welcome to the house price prediction API'}

@app.post('/predict', response_model=outputSchema)
def predict(user_input: InputSchmema):
    prediction= make_prediction(user_input.model_dump())
    return outputSchema(predicted_price=round(prediction, 2))