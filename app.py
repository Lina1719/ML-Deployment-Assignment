from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# uncomment and load your model file and other files if you have (encoder/scaler)
# encoder = pickle.load(open('your_encoder.pkl', 'rb'))
# model = pickle.load(open('your_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():

    # get features and values from the user
    data = request.form.to_dict()
    

    return render_template('predictions.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)