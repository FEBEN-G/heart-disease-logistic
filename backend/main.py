from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Heart Disease Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained Logistic Regression model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model/logistic_model.joblib")
lr_model = None

try:
    lr_model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")

class HeartData(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: float
    thal: int

@app.post("/predict")
def predict(data: HeartData):
    if lr_model is None:
        raise HTTPException(status_code=500, detail="Logistic Regression model not loaded")
    
    features = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol, 
        data.fbs, data.restecg, data.thalach, data.exang, 
        data.oldpeak, data.slope, data.ca, data.thal
    ]])
    
    try:
        prediction = lr_model.predict(features)
        probability = lr_model.predict_proba(features)[0][1]
        
        return {
            "prediction": int(prediction[0]),
            "probability": float(probability),
            "status": "Healthy" if prediction[0] == 0 else "Heart Disease Risk",
            "message": "Prediction successful"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {
        "status": "healthy", 
        "logistic_loaded": lr_model is not None
    }
