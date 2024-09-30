import joblib
import numpy as np

from tensorflow.keras.models import load_model

model = load_model('Crop_Recommendation_system/models/new.keras')

def predict_crop(temp,hum,grain,vege,crop,fruit):
    try:
        
        input_data = np.array([[temp,hum,grain,vege,crop,fruit]]).reshape(1,-1)

        prediction = model.predict(input_data)

        predicted_class = np.argmax(prediction,axis=1)[0]
        return (predicted_class)
    
    except Exception as e:
        raise RuntimeError(f"Error in prediction: {str(e)}")
