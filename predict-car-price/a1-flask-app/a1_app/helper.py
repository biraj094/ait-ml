import pickle
from a1_app import application
import numpy as np
from sklearn.preprocessing import StandardScaler 



def get_predicted_values(model_values):
    #Load the model
    model_path = application.root_path+'/static/a1m1.model'
    saved_model = pickle.load(open(model_path, 'rb'))

    # Load the scaler and scale the values that the user entered
    scaler_path = application.root_path+'/static/scaler.pkl'
    scaler = pickle.load(open(scaler_path, 'rb'))
    # scaler = StandardScaler()
    predicted_price = saved_model.predict(scaler.transform(model_values))

    # Scale the output so that user understands the output
    final_predicted_price = np.exp(predicted_price)

    return round(final_predicted_price[0],2)
