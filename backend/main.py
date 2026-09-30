from fastapi import FastAPI
from backend.schemas import model_input
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

model = joblib.load('models/RF_model.pkl')


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://saadaliasghar1045-ops.github.io"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    probabilities = model.predict_proba(features)[0]
    
    predicted_index = list(model.classes_).index(prediction)
    confidence = probabilities[predicted_index]
    return {
        "recommended_crop":prediction[0], # writing prediction[0] because it returns a list like ['rice] and prediction[0] returns simply rice
        "Confidence":round(float(confidence),2)
    }