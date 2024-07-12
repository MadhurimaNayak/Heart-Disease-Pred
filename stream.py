import numpy as np
import pickle
import streamlit as st
import os

model_path = 'trained_model.sav'

if not os.path.isfile(model_path):
    import requests
    url = 'https://drive.google.com/file/d/1ZyCh0_pdNCXCxizzO-2Hbzl8WAh60_HD/view?usp=sharing'
    response = requests.get(url)
    with open(model_path, 'wb') as f:
        f.write(response.content)

loaded_model = pickle.load(open(model_path, 'rb'))

def heart_pred(input_data):
    
    input_fin=np.asarray(input_data).reshape(1,-1)
    pred=loaded_model.predict(input_fin)
    print(pred)
    if(pred[0]==0):
       return 'Absence of heart disease'
    else:
        return 'Presence of heart disease'
    
def main():
    
    st.title('Heart Disease Prediction')

    Age=st.text_input('Age of patient in years')
    Gender=st.text_input('Gender of patient')
    Chestpain=st.text_input('Chest Pain Type')
    Restingbp=st.text_input('Resting Blood Pressure (mm HG)')
    Cholestrol=st.text_input('Serum Cholestrol (mg/dl)')
    Fastingblsugar=st.text_input('Fasting Blood sugar')
    Restelect=st.text_input('Resting electrocardiogram results')
    Maxheart=st.text_input('Maximum Heart Rate achieved')
    Exangia=st.text_input('Exercise Induced Angia')
    Oldpeak=st.text_input('Oldpeak')
    Slope=st.text_input('Slope of the peak exercise ST segment')
    Bloodves=st.text_input('Number of major blood vessels damaged')

    diagnosis=''

    if st.button('Result'):
        diagnosis=heart_pred([Age,Gender,Chestpain,Restingbp,Cholestrol,Fastingblsugar,Restelect,Maxheart,Exangia,Oldpeak,Slope,Bloodves])

    st.success(diagnosis)


if __name__=='__main__':
    main()




