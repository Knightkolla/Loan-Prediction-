from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load('model/loan_rfc_model.pkl')


def predict_loan(data):
    try:
        
        features = np.array([
            data['Gender'][0],
            data['Married'][0],
            data['Dependents'][0],
            data['Education'][0],
            data['Self_Employed'][0],
            data['ApplicantIncome'][0],
            data['CoapplicantIncome'][0],
            data['LoanAmount'][0],
            data['Loan_Amount_Term'][0],
            data['Credit_History'][0],
            data['Property_Area'][0]
        ]).reshape(1, -1).astype(float)
        
 
        
        proba = model.predict_proba(features)[0]
        prediction = model.predict(features)[0]
        
        return ('Approved', proba[1] * 100) if prediction == 1 else ('Rejected', proba[0] * 100)
    
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return 'Error', 0.0

@app.route('/')
def home():
    return render_template('index.html', prediction='', probability='0%', features={})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = {
            'Gender': request.form['Gender'],
            'Married': request.form['Married'],
            'Dependents': request.form['Dependents'],
            'Education': request.form['Education'],
            'Self_Employed': request.form['Self_Employed'],
            'ApplicantIncome': request.form['ApplicantIncome'],
            'CoapplicantIncome': request.form['CoapplicantIncome'],
            'LoanAmount': request.form['LoanAmount'],
            'Loan_Amount_Term': request.form['Loan_Amount_Term'],
            'Credit_History': request.form['Credit_History'],
            'Property_Area': request.form['Property_Area']
        }
        
      
        for key in form_data:
            form_data[key] = [float(form_data[key])]
            
        df = pd.DataFrame(form_data)
  
        prediction, probability = predict_loan(df)
        
        return render_template('index.html',
                               prediction=prediction,
                               probability=f"{probability:.1f}%",
                               features=form_data)
    
    except Exception as e:
        print(f"Exception during prediction: {str(e)}")
        return render_template('index.html', 
                               prediction=f'Error: {str(e)}',
                               probability='0%',
                               features={})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
