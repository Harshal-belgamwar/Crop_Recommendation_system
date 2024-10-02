from flask import Flask,request,jsonify,render_template
import joblib
from models.model import predict_crop
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

crop_mapping = {
    0:"TOMATO",
    1:"COFFEE",
    2:"COTTON",
    3:"JUTE",
    4:"MANGO",
    5:"ORANGE",
    6:"RICE"
}

@app.route('/predict',methods = ['POST'])
def predict():
    try:
        
        hum = float(request.form.get('humidity'))
        temp = float(request.form.get('temp'))
        grain = int(request.form.get('grain',0))
        vege = int(request.form.get('vege',0))
        crop = int(request.form.get('crop',0))
        fruit = int(request.form.get('fruit',0))
 
        temp = ((temp)/35.99009679)
        hum = ((hum)/94.96419851)

        prediction = predict_crop(temp,hum,grain,vege,crop,fruit)
        output = f"Predicted crop ID: {prediction}"

        # Encoded value 0 corresponds to: Tomato
        # Encoded value 1 corresponds to: coffee
        # Encoded value 2 corresponds to: cotton
        # Encoded value 3 corresponds to: jute
        # Encoded value 4 corresponds to: mango
        # Encoded value 5 corresponds to: orange
        # Encoded value 6 corresponds to: rice
        print(f"Received Data - Temperature: {temp}, Humidity: {hum}, Grain: {grain}, Vegetable: {vege}, Crop: {crop}, Fruit: {fruit}")

        predicted = crop_mapping.get(prediction,"Unknown")

        return render_template('index.html', prediction_text = predicted)
    except Exception as e:
        return str(e)
    
if __name__=='__main__':
    app.run(debug=True)


