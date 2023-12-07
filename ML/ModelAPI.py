from flask import Flask, request, jsonify
import joblib
import pandas as pd
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)


CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

# To start Flask api. In command line
# $ python ModelAPI.py it will provided URL
# usually http://127.0.0.1:5000/predict format to request prediction example see testAPI.py below is output example

# (base) davidarteaga@davids-macbook-pro ML % python testAPI.py
# JSON Response: {'prediction': 'Moderate'}

# Load the model
model = joblib.load('pipelineFINAL.joblib')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Extract data from POST request
#         data = request.get_json()
#
#         # data is a dictionary with keys: 'Date', 'Max Temperature (F)', 'Min Temperature (F)'precipitation (mm)'
#
#         # Create a DataFrame from json data
#         df = pd.DataFrame([data])
#
#         # Make prediction from loaded model
#         prediction = model.predict(df)
#
#         # Return prediction back in json format
#         return jsonify({'prediction': prediction[0]})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
# if __name__ == '__main__':
#     app.run(debug=True)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from POST request
        data = request.get_json()

        date_parsed = datetime.strptime(data['Date'], '%Y-%m-%d')
        data['Year'] = date_parsed.year
        data['Month'] = date_parsed.month
        data['Day'] = date_parsed.day

        del data['Date']

        # Create a DataFrame from json data
        df = pd.DataFrame([data])

        # Ensure the DataFrame columns order matches the model's expected input
        expected_columns = ['Year', 'Month', 'Day', 'Max Temperature (F)', 'Min Temperature (F)', 'Precipitation (mm)']
        df = df[expected_columns]

        # Make prediction from loaded model
        prediction = model.predict(df)

        # Return prediction back in json format
        return jsonify({'prediction': prediction[0].tolist()})
    except Exception as e:
        return jsonify({'error': 'Error processing request: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
