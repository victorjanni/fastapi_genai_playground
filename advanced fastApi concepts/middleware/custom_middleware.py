from fastapi import FastAPI, Request
import time
from starlette.middleware.base import BaseHTTPMiddleware

app=FastAPI()

class TimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f'Request: {request.url.path} processed in {duration:.5f} seconds')
        return response

app.add_middleware(TimeMiddleware)

@app.get('/hello')
async def hello():
    for _ in range(1000000):
        pass
    return {'message': 'Hello, World!'}
        
