from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
import src.pipeline.predict_pipeline as pp

application = Flask(__name__)

app = application

# Route for home page

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=['GET', 'Post'])
def predict_datapoint():
    #if get then go to the home page 
    if request.method =="GET":
        return render_template('home.html')
    # if post then use the input data of the form to make the eprediction and return result
    else:
        # create a dataframe from the input. 
        data=pp.CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=pp.PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")       