from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as pickle_file:
    pipe = pickle.load(pickle_file)

@app.route('/')
def welcome_message():
  return 'Please go to 127.0.0.1:5000/homepage for further instruction'

@app.route('/homepage')
def home():
  return 'Hi! Welcome to the prediction site. Please go to http://127.0.0.1:5000/predict to make predictions'

@app.route('/predict',methods=['POST'])
def predict():
  if request.method == 'POST':
    the_data = request.get_json(force=True)
    newdata = the_data['newdata']
    predictions = pipe.predict_proba(newdata)
    return jsonify(predictions.tolist())

