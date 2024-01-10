from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello_world():
  return { "status": 200, "data": { "message": "Hello World!" }}