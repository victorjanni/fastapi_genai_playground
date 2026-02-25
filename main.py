from typing import Annotated, Literal

from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
import json

app=FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='Unique identifier for the patient', example='P001')]
    name: Annotated[str,Field(..., description='Full name of the patient', example='John Doe')]
    city: Annotated[str, Field(..., description='City of residence', example='New York')]
    age: Annotated[int, Field(...,gt=0, lt=120, description='Age of the patient', example=30)]
    gender: Annotated[Literal['Male', 'Female', 'Others'], Field(..., description='Gender of the patient', example='Male')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in cm', example=175.5)]
    weight: Annotated[float, Field(..., gt=0,description='Weight of the patient in kg', example=70.0)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5 :
            return "underweight"
        elif self.bmi < 25:
            return "normal weight"
        elif self.bmi < 30:
            return "overweight" 
        else:
            return "obese"


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data   
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f) 

@app.get("/")
def hello():
    return {'message':'hi victor'}

@app.get("/about")
def about():
    return {'message': 'Patient Management System API'}

@app.get("/products")
def products():
    return {'message':'A fully functional API to manage your patient reccords'}

@app.get('/view')
def view():
    data = load_data()

    return data
 
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort on the basis of height, weight or bmi'), 
                  order: str = Query('asc', description='sort in asc desc order')):
    valid_fields= ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='invalid order select between asc and desc')
    
    data=load_data()
    sort_order= True if order=='desc' else False

    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data
@app.post('/create')
def create_patient(patient: Patient):

    #load existing data
    data = load_data()

    #check if patient id already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient with this ID already exists')
    
    #add new patient to data
    data[patient.id]=patient.model_dump(exclude=['id'])
    # save updated data back to file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})


