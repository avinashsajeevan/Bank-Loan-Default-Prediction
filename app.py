import streamlit as st
import pandas as pd
import numpy as np
import pickle

# loading the trained model
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


# defining the function which will make the prediction using the data which the user inputs
def prediction(age, ed, employ, address, income, debtinc, creddebt, othdebt):
    input_dict = {'age' : age,
               "ed" : ed,
               "employ" : employ,
               "address" : address,
                "income" : income,
              "debtinc" : debtinc,
              "creddebt" : creddebt,
                "othdebt" : othdebt}
    input_df = pd.DataFrame([input_dict])
    predict1 = model.predict_proba(input_df)[:, 1]
    if predict1 >= 0.473647:
        c = "Default"
    else:
        c = "No default"
    return c



# this is the main function in which we define our webpage
def run():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Bank Loan Default Prediction App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    age = st.number_input('Age of Customer', min_value=18, max_value=100, value=18)
    ed = st.number_input('Education Category', min_value=0, value=1)
    employ = st.number_input('Employment status', min_value=0, value=18)
    address = st.number_input('Geographic area', min_value=0, value=2)
    income = st.number_input('Gross Income', value=0.1, step=0.01)
    debtinc = st.number_input('Individuals debt', value=0.1, step=0.01)
    creddebt = st.number_input('Debt-to-Credit Ratio', value=0.1, step=0.01)
    othdebt = st.number_input('Any other debts', value=0.1, step=0.01)
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(age, ed, employ, address, income, debtinc, creddebt, othdebt)
        st.success('Prediction: {}'.format(result))

run()
