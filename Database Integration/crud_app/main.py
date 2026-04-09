import models, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# endpoints
# 1.create an employee
@app.post('/employees', response_model=schemas.Employeeout)  
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee) 

# 2.get all employees
@app.get('/employees', response_model=list[schemas.Employeeout])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

# 3.get an employee by id
@app.get('/employees/{emp_id}', response_model=schemas.Employeeout)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='employee not found')
    return employee

# 4.update an employee
@app.put('/employee/{emp_id}', response_model=schemas.Employeeout)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='employee not found')
    return db_employee

# 5.delete an employee
@app.delete('/employee/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='employee not found')
    # return employee
    return {'detail': 'employee deleted successfully'}    
    