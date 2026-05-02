from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30

def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    
    payload = data.copy()
    payload.update({'exp': expire})

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')

        if username is None:
            raise HTTPException(status_code=401, detail='token missing')

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="couldn't validate credentials")