# -*- coding: utf-8 -*-
"""
Created on Mon May 19 22:07:17 2025

@author: shrey
"""

from fastapi import FastAPI
from pydantic import BaseModel #to setup the format in which the data will be posted to our API
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFuntion:float
    Age:int


#loading the saved model
diabetes_model=pickle.load(open('diabetes_model.sav','rb'))


@app.post('/diabetes_prediction') 
def diabetes_pred(input_parameters:model_input):
    
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)


    preg=input_dictionary['Pregnancies']
    glu=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dpf=input_dictionary['DiabetesPedigreeFuntion']
    age=input_dictionary['Age']


    input_list=[preg,glu,bp,skin,insulin,bmi,dpf,age]

    prediction=diabetes_model.predict([input_list]) #we are putting the list within the list to clarify we are trying to predict for only one data point

    if prediction[0]==0:
        return'The person is not Diabetic'

    else:
        return 'The person is Diabetic'














