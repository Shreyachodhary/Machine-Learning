# -*- coding: utf-8 -*-
"""
Created on Tue May 20 00:04:49 2025

@author: shrey
"""

import json
import requests

url=' http://127.0.0.1:8000/diabetes_prediction'


input_data_for_model={
    
    'Pregnancies':6,
    'Glucose':148,
    'BloodPressure':72,
    'SkinThickness':35,
    'Insulin':0,
    'BMI':33.6,
    'DiabetesPedigreeFuntion':0.627,
    'Age':50 
    
    }

input_json=json.dumps(input_data_for_model)

response=requests.post(url,data=input_json)

print(response.text)
