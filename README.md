# 🌱 Crop Recommender

A machine learning application that recommends a suitable crop based on soil and environmental conditions.

This project started as a way for me to practice the concepts I learned from Andrew Ng's Machine Learning course and apply them to a real-world problem. I wanted to go beyond a simple Jupyter Notebook and build a complete application with a machine learning model, backend API, and frontend.

## 🎯 Problem

Choosing a suitable crop can be difficult for farmers, especially when considering different soil and environmental conditions.

The goal of this project is to use machine learning to learn patterns from crop data and provide a crop recommendation based on:

* Nitrogen (`N`)
* Phosphorus (`P`)
* Potassium (`K`)
* Temperature
* Humidity
* Soil pH
* Rainfall

## 🤖 Machine Learning Model

The final model used in the application is a **Random Forest Classifier** trained on the Crop Recommendation dataset.

The dataset contains:

* **2,200 samples**
* **22 crop classes**
* **7 input features**

The trained model is saved as:

```text
models/RF_model.pkl
```

The model achieved approximately **99.32% accuracy** on the test set.

## 🏗️ Application Architecture

The project is divided into three main parts:

```text
                 User
                  │
                  ▼
        ┌──────────────────┐
        │     Frontend     │
        │   HTML/CSS/JS    │
        └────────┬─────────┘
                 │
                 │ POST /predict
                 ▼
        ┌──────────────────┐
        │   FastAPI API    │
        │                  │
        │  Random Forest   │
        └────────┬─────────┘
                 │
                 ▼
        Recommended Crop
```

### Components

**Machine Learning**

The model was developed and evaluated in `main.ipynb`.

**Backend**

A FastAPI application loads the trained Random Forest model and provides a `/predict` API endpoint.

**Frontend**

A separate frontend application provides a simple interface where users can enter the required soil and environmental values.

## 📁 Backend Project Structure

```text
crop-recommender/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── models/
│   └── RF_model.pkl
│
├── main.ipynb
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## 🔌 API

The backend exposes a prediction endpoint:

```text
POST /predict
```

Example request:

```json
{
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.8,
    "humidity": 82.0,
    "ph": 6.5,
    "rainfall": 202.9
}
```

Example response:

```json
{
    "recommended_crop": "rice"
}
```

## 🛠️ Technologies

### Machine Learning

* Python
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Random Forest

### Backend

* FastAPI
* Pydantic
* Joblib
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Development

* Jupyter Notebook
* Git
* GitHub
* uv

## 🚀 Project Status

* [x] Dataset exploration
* [x] Data preparation
* [x] Model training
* [x] Model evaluation
* [x] Random Forest model
* [x] Model serialization
* [x] FastAPI backend
* [x] Backend deployment
* [ ] Frontend development
* [ ] Frontend deployment

## 📌 Future Improvements

Some possible improvements for future versions include:

* Improve the frontend user experience
* Add input validation on the frontend
* Add more agricultural data
* Experiment with additional machine learning models
* Improve the model using more representative real-world data
* Add more information about the recommended crop

## 👨‍💻 About This Project

This is one of my first projects where I am taking a machine learning model beyond a Jupyter Notebook and turning it into a working application.

The purpose of the project is not only to train a model, but also to learn how different parts of a machine learning application work together:

```text
Machine Learning
       +
    Backend
       +
    Frontend
       =
 Working ML Application
```

