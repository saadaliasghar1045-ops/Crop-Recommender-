from fastapi import FastAPI
from backend.schemas import model_input

app = FastAPI()


@app.post("/predict")
def home(data : model_input):
    out = {
        "message":"This endpoint is working",
        "Input":data
    }
    return out