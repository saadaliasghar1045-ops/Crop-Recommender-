from fastapi import FastAPI
from backend.schemas import model_input
import joblib

app = FastAPI()

model = joblib.load('models/RF_model.pkl')

@app.get("/")
def home():
    return {"message": "Crop Recommender API is running!"}


@app.post("/predict")
async def predict_crop(data : model_input):
    # converting data into 2D list for prediction
    features = [[
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]]
    prediction = model.predict(features)
    return {
        "recommended_crop":prediction[0] # writing prediction[0] because it returns a list like ['rice] and prediction[0] returns simply rice
    }