# Heart Disease Prediction System

A professional end-to-end machine learning application that predicts the risk of heart disease using **Logistic Regression**. The project includes a high-performance **FastAPI** backend and a premium **Glassmorphism UI** frontend.

## 🚀 Key Features
- **End-to-End ML Pipeline**: Data cleaning, scaling, training, and evaluation in a Google Colab-style notebook.
- **Logistic Regression Model**: Optimized for ~85% accuracy on the UCI Heart Disease dataset.
- **FastAPI Backend**: Robust REST API for real-time risk assessment.
- **Premium UI**: Modern, responsive dashboard with animations and real-time visualization.
- **Health Monitoring**: Built-in health check endpoints for server monitoring.

## 📂 Project Structure
```text
.
├── backend/            # FastAPI Application & ML Model
│   ├── model/          # Trained .joblib models
│   ├── main.py         # Primary API script
│   └── requirements.txt
├── frontend/           # Modern Dashboard (HTML/CSS/JS)
│   └── index.html
├── notebook/           # ML Experimentation & Pipeline
│   └── logistic_pipeline.ipynb
├── data/               # Project Dataset
│   └── heart.csv
└── train_model.py      # Automated Model Training Utility
```

## 🛠️ Quick Start

### 1. Model Training
If you wish to retrain the model:
```bash
# Set up environment
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

# Run training
python train_model.py
```

### 2. Run Backend
```bash
cd backend
python -m uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### 3. Run Frontend
Simply open `frontend/index.html` in any modern web browser or use a live server extension.

## 📈 ML Pipeline Detail
The pipeline leverages `scikit-learn`:
1. **Imputation**: Handles missing values using median distribution.
2. **Scaling**: Implements `StandardScaler` to normalize feature variance.
3. **Algorithm**: Logistic Regression with 1000 max iterations for convergence.
4. **Export**: The entire pipeline (Scaler + Model) is saved as a single object for consistency.
