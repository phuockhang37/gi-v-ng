from flask import Flask, render_template, request, jsonify
from Backend import predict_price

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    try:
        data = request.get_json()
        # Predict the price using the selected model
        predicted_price = predict_price(data)
        return jsonify({'success': True, 'predicted_price': float(predicted_price)})

    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


