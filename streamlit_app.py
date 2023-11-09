import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("D:\Prediction\prediction.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(Shift,Item,Oper_num,eff,qlt_perc,Target_qty,Rej_qty,worked_min,bal_min): 
    prediction=classifier.predict([[Shift,Item,Oper_num,eff,qlt_perc,Target_qty,Rej_qty,worked_min,bal_min]])
    print(prediction)
    return prediction
def main():
    st.title("Quantity Prediction")
    #date_input = st.sidebar.date_input('Select a Date')
    #date_timestamp = pd.to_datetime(date_input).timestamp()
    #curr_date= st.date_input("Enter Date (YYYY/MM/DD)").timestamp()
    Shift = st.text_input("Shift")
    Item = st.text_input("Item")
    if(Item == 'DC2A210235'):
        Item = 1
    elif(Item == 'TVS-SPG-288'):
        Item = 3
    elif(Item == 'DC2A210238'):
        Item = 2
    elif(Item == 'AC2A110015'):
        Item = 0
    Oper_num = st.text_input("Operator number")
    eff = st.text_input("Efficiency")
    qlt_perc = st.text_input("Quality percentage")
    Target_qty = st.text_input("Target quantity")
    Rej_qty = st.text_input("Rejected quantity")
    worked_min = st.text_input("Worked minutes")
    bal_min = st.text_input("Balance minutes")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Shift,Item,Oper_num,eff,qlt_perc,Target_qty,Rej_qty,worked_min,bal_min)
    st.success('The output is {}'.format(result))
    

if _name=='main_':
    main()
