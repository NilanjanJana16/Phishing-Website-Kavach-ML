#importing required libraries

from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction
from flask_cors import CORS


file = open("pickle/model.pkl","rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('index.html',xx =round(y_pro_non_phishing,2),url=url )
    return render_template("index.html", xx =-1)

@app.route("/api", methods=["POST"])
def predict_api():
    # Get the input data from the request
    data = request.get_json()
    
    # Extract features from the input URL using FeatureExtraction
    url = request.json.get("url")
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1,30) 
    
    y_pred =gbc.predict(x)[0]
    
    
    # Return the prediction as a JSON response
    if y_pred == 1:        
        response = {
            # return True
            "prediction": "safe",
            "score": gbc.predict_proba(x)[0,1]*100  #probability of that it is closer to 1 
        }
        
    if y_pred == -1:
        response={
           # return False
           "prediction": "unsafe",
           "score": gbc.predict_proba(x)[0,0]*100 #probability of that it is closer to -1
    }
        
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
