from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello First API slash"}


@app.get("/api/v1/ping")
async def ping():
    return {"message": "Hello First API w Path"}


# API 2: GET /api/v1/greeting
@app.get("/api/v1/greeting")
async def greeting():
    return {"greeting": "Hello API 2"}


# API 3: GET /api/v1/greeting/pradeep Pradeep is a variable
'''
from the Fast API docs: https://fastapi.tiangolo.com/tutorial/path-params/
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id} 
'''
@app.get("/api/v1/greeting/{pradeep}")
async def read_item(pradeep):
    return {"pradeep": "testing " + pradeep}

# API 4: GET /api/v1/sum/1/1
@app.get("/api/v1/sum/{V1}/{V2}")
async def read_item(V1):
    return {"result": V1+V2}

