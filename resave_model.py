import joblib

# Load the existing model
model = joblib.load('LR_AQI_Prediction.joblib')

# Resave with current joblib to fix compatibility
joblib.dump(model, 'LR_AQI_Prediction_updated.joblib')

print("Model resaved successfully.")