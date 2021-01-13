import streamlit as st
import numpy as np
import pickle
model = pickle.load(open('model.pkl','rb'))

def predict_loan(ApplicantIncome ,CoapplicantIncome ,LoanAmount,Loan_Amount_Term,Credit_History):
    input = np.array([[ApplicantIncome ,CoapplicantIncome ,LoanAmount, Loan_Amount_Term,Credit_History]]).astype(np.float64)
    prediction = model.predict(input) 
    return prediction

def main():
    st.title("ML App")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:centre;">Loan Prediction</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html = True)
     
    Name = st.text_input("Name")
    Age = st.text_input("Age")
    ApplicantIncome = st.text_input("ApplicantIncome(In Rupees)")
    CoapplicantIncome = st.text_input("CoapplicantIncome(In Rupees)")
    LoanAmount = st.text_input("LoanAmount(In Rupees)")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term(In Days)")
    Credit_History = st.text_input("Credit_History")

    accept_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your Loan is accepeted</h2>
       </div>
    """

    refuse_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your Loan is refused</h2>
       </div>
    """
    
    if st.button("Predict"):
        output = predict_loan(ApplicantIncome ,CoapplicantIncome ,LoanAmount,Loan_Amount_Term,Credit_History)

        if output == 'Y':
            st.markdown(accept_html,unsafe_allow_html = True)
        else:
            st.markdown(refuse_html,unsafe_allow_html = True)


if __name__=='__main__':
    main()

