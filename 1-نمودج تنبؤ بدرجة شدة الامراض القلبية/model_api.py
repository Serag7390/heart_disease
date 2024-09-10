from flask import Flask, request, jsonify, render_template
import pandas as pd
from joblib import load

app = Flask(__name__)


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
        
        
        pred_class = model.predict(transformed_data)
        
        
        response = {
            'predicted_class': int(pred_class[0])
        }
        
        return render_template('result.html', predicted_class=int(pred_class[0]))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
