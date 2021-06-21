#realestateDatainput=open("C:/Users/ANTHONY/Desktop/important ipynb codes/realestatedataproject.csv","r",newline="")
from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('C:/Users/ANTHONY/Desktop/important ipynb codes/REGRESSION/LOR/deploying/LOG_REG_Cleveland.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')




standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        Age = int(request.form['Age'])
        trestbps=int(request.form['trestbps'])
        thalach=int(request.form['thalach'])
        oldpeak=int(request.form['oldpeak'])
        
        ##################
        Sex_0=int(request.form['Sex_0'])
        if(Sex_0==0):
            Sex_0=1
            Sex_1=0
        else:
            Sex_0=0
            Sex_1=1      
        ##################
        cp_1=int(request.form['cp_1'])
        if(cp_1==1):
            cp_1=1
            cp_2=0
            cp_3=0
            cp_4=0
        elif(cp_1==2):
            cp_1=0
            cp_2=1
            cp_3=0
            cp_4=0
        elif(cp_1==3):
            cp_1=0
            cp_2=0
            cp_3=1
            cp_4=0
        else:
            cp_1=0
            cp_2=0
            cp_3=0
            cp_4=1
        ##################
        fbs_0=int(request.form['fbs_0'])
        if(fbs_0==0):
            fbs_0=1
            fbs_1=0
        else:
            fbs_0=0          
            fbs_1=1   
        ##################
        restecg_0=int(request.form['restecg_0'])
        if(restecg_0==0):
            restecg_0=1
            restecg_1=0
            restecg_2=0
        elif(restecg_0==1):
            restecg_0=0
            restecg_1=1
            restecg_2=0 
        else:
            restecg_0=0
            restecg_1=0
            restecg_2=1
             
       
        ##################
        exang_0=int(request.form['exang_0'])
        if(exang_0==0):
            exang_0=1
            exang_1=0
        else:
            exang_0=0
            exang_1=1          
        ##################
        slope_1=int(request.form['slope_1'])
        if(slope_1==1):
            slope_1=1
            slope_2=0
            slope_3=0
        elif(slope_1==2):
            slope_1=0
            slope_2=1
            slope_3=0 
        else:
            slope_1=0
            slope_2=0
            slope_3=1
        ##################
        ca_0=int(request.form['ca_0'])
        if(ca_0==0):
            ca_0=1
            ca_1=0
            ca_2=0
            ca_3=0
        elif(ca_0==1):
            ca_0=0
            ca_1=1
            ca_2=0
            ca_3=0
        elif(ca_0==2):
            ca_0=0
            ca_1=0
            ca_2=1
            ca_3=0
        else:
            ca_0=0
            ca_1=0
            ca_2=0
            ca_3=1
        ##################    
        thal_3=int(request.form['thal_3'])
        if(thal_3==3):
            thal_3=1
            thal_6=0
            thal_7=0
        elif(thal_3==7):
            thal_3=0
            thal_6=1
            thal_7=0 
        else:
            thal_3=0
            thal_6=0
            thal_7=1
        prediction=model.predict([[Age, trestbps, thalach, oldpeak, Sex_0, Sex_1, cp_1,
       cp_2, cp_3, cp_4, fbs_0, fbs_1, restecg_0, restecg_1,
       restecg_2, exang_0, exang_1, slope_1, slope_2, slope_3,
       ca_0, ca_1, ca_2, ca_3, thal_3, thal_6, thal_7]])
        output=round(prediction[0],2)
        #if output==0:
         #   return render_template('index.html',prediction_text="000000")
        #else:
         #   return render_template('index.html',prediction_text="1111")

        if int(round(prediction[0],2)) == 0:
            result = " - You do not have a heart disease"
        elif int(round(prediction[0],2)) == 1:
            result = "- You have a heart disease"
        else:
            result="SORRY CANNOT FIGURE IT OUT"
            
        return render_template('index.html',prediction_texts=result)

if __name__=="__main__":
    app.run(port=5000,debug=True)