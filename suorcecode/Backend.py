import joblib
import numpy as np

# Load pre-trained models
ada_model = joblib.load('ada_model.pkl')
xgb_model = joblib.load('xgb_model.pkl')
lgb_model = joblib.load('lgb_model.pkl')

def preprocess_input(data):
    """Convert user input into a format suitable for model prediction."""
    try:
        # Convert input values to floats
        features = [float(data[key]) for key in ['open', 'high', 'low', 'vol', 'change']]
        return np.array(features).reshape(1, -1)
    except ValueError:
        raise ValueError("Invalid input! Please enter numerical values.")

def predict_price(input_data):
    """Predicts the price based on the selected model."""
    # Preprocess user input
    features = preprocess_input(input_data)

    # Predict using the selected model
    if input_data['model'] == 'ada':
        prediction = ada_model.predict(features)
    elif input_data['model'] == 'xgb':
        prediction = xgb_model.predict(features)
    elif input_data['model'] == 'lgb':
        prediction = lgb_model.predict(features)
    else:
        raise ValueError("Invalid model selected")

    return float(prediction[0])
