import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Create directories if they don't exist
os.makedirs('backend/model', exist_ok=True)

# Load dataset
df = pd.read_csv("data/heart.csv", encoding='utf-8-sig')

# Data Preprocessing
df.fillna(df.median(), inplace=True)

# Split features and target
X = df.drop("target", axis=1)
y = df["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Logistic Regression Pipeline
lr_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])
lr_pipeline.fit(X_train, y_train)

# Save model
joblib.dump(lr_pipeline, "backend/model/logistic_model.joblib")

print("Logistic Regression model trained and saved successfully.")
print(f"LR Accuracy: {accuracy_score(y_test, lr_pipeline.predict(X_test)):.4f}")
