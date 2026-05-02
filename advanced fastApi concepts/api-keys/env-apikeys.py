from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic_settings import BaseSettings

class settings(BaseSettings):
    api_key: str

    class config:
        env_file ='.env'

settings= settings()
app = FastAPI()

def get_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="unauthorized")
    return api_key

@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {"output": "Access granted"}