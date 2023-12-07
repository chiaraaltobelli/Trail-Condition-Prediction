import requests


url = 'http://127.0.0.1:5000/predict'
#data should be sent in this specific format.
data = {
    'Date': '2023-01-01',
    'Max Temperature (F)': 50,
    'Min Temperature (F)': 40,
    'Precipitation (mm)': 0.1
}

response = requests.post(url, json=data)

# Print the predicted response else failed
if response.status_code == 200:
    # print("JSON Response:", response.json())

    json_response = response.json()

    prediction = json_response.get('prediction', [])

    labels = ['Avoid', 'Alternatives', 'All Weather', 'Good Bets']

    # Print each label with its corresponding prediction
    print("Predictions:")
    for label, pred in zip(labels, prediction):
        print(f" - {label}: {pred}")
else:
    print("Failed to get response")
