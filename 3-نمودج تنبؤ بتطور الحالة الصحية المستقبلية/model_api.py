from flask import Flask, request, jsonify, render_template
import pandas as pd
from joblib import load

app = Flask(__name__)


class Model:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_input):
        predicted_num = self.model.predict(X_input)
        return [self.map_health_status(value) for value in predicted_num]

    def map_health_status(self, num_value):
        if num_value == 0:
            return "Condition improves"
        elif num_value == 1:
            return "stability"
        elif num_value == 2:
            return "Mild deterioration"
        elif num_value == 3:
            return "Moderate deterioration"
        elif num_value == 4:
            return "Serious deterioration"
        else:
            return "unknown"






model = load("classification_model.pkl")
scaler = load("standard_scaler.pkl")
labelencoder_sex = load("sex_label_encoder.pkl")
labelencoder_fbs = load("fbs_label_encoder.pkl")
labelencoder_exang = load("exang_label_encoder.pkl")
ct_loaded = load("ct_column_transformer.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
       
        data = request.form
        
        
        example_df = pd.DataFrame({
            'age': [data['age']],
            'sex': [data['sex']],
            'dataset': [data['dataset']],
            'cp': [data['cp']],
            'trestbps': [data['trestbps']],
            'chol': [data['chol']],
            'fbs': [data['fbs']],
            'restecg': [data['restecg']],
            'thalch': [data['thalch']],
            'exang': [data['exang']],
            'oldpeak': [data['oldpeak']],
            'slope': [data['slope']],
            'ca': [data['ca']],
            'thal': [data['thal']]
        })
        
        
        example_df['sex'] = labelencoder_sex.transform(example_df['sex'])
        example_df['fbs'] = labelencoder_fbs.transform(example_df['fbs'])
        example_df['exang'] = labelencoder_exang.transform(example_df['exang'])
        example_df = ct_loaded.transform(example_df)
        
        
        transformed_data = scaler.transform(example_df)
        
        
        pred_health_status = model.predict(transformed_data)
        
        
        response = {
            'predicted_class': (pred_health_status[0])
        }
    
        return render_template('result.html', predicted_class=(pred_health_status[0]))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
