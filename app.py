from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import pandas as pd


model = joblib.load("Linear_regressor_FIAT500.pkl")
encoders = joblib.load("label_encoders.pkl")
StandardScaler_X  = joblib.load("standard_scaler.pkl")
LabelEncoder_model = encoders["model"]
LabelEncoder_transmission = encoders["transmission"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print("endpoint raggiunto")
    try:

        data = request.json

        model_type = data['model']
        engine_power = data['engine_power']
        transmission = data['transmission']
        age_in_days = data['age_in_days']
        km = data['km']
        previous_owners = data['previous_owners']
        
        user_input = np.array([model_type, engine_power, transmission, age_in_days, km, previous_owners])
        print(user_input)
        user_input_model_encoded = LabelEncoder_model.transform(user_input[0].reshape(-1))
        user_input_transmission_encoded = LabelEncoder_transmission.transform(user_input[2].reshape(-1))
        df = pd.DataFrame([user_input], columns=["model", 	"engine_power" ,	"transmission" ,	"age_in_days" 	,"km" 	,"previous_owners"])
        user_input_norm = StandardScaler_X.transform(df[["engine_power","age_in_days", "km", "previous_owners"]])
        user_input_to_predict = np.insert(user_input_norm, 0, user_input_model_encoded, axis=1)

        user_input_to_predict = np.insert(user_input_to_predict, 2, user_input_transmission_encoded, axis=1)
        prediction = model.predict(user_input_to_predict)
        print(prediction)
        return jsonify({
            'price': float(prediction[0])
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)