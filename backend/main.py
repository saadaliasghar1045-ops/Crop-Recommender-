from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Crop Recommender API is running!"}