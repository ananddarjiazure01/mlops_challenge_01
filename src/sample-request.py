import urllib.request
import json

# 👇 Request body — must match your model’s schema
data = {
    "input_data": {
        "columns": [
            "PatientID",
            "Pregnancies",
            "PlasmaGlucose",
            "DiastolicBloodPressure",
            "TricepsThickness",
            "SerumInsulin",
            "BMI",
            "DiabetesPedigree",
            "Age"
        ],
        "data": [
            # One sample input (you can add multiple rows)
            [1, 2, 138, 62, 35, 0, 33.6, 0.127, 47]
        ]
    },
    "params": {}
}

# Convert Python dict → JSON bytes
body = str.encode(json.dumps(data))

# Your endpoint URL
url = "https://github-endpoint.centralindia.inference.ml.azure.com/score"

# Your endpoint key
api_key = "YOUR_API_KEY_HERE"
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# HTTP headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

# Send request
req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read().decode("utf-8")
    print("✅ Prediction result:\n", result)
except urllib.error.HTTPError as error:
    print("❌ Request failed with status code:", error.code)
    print("Headers:", error.info())
    print("Body:", error.read().decode("utf8", "ignore"))
