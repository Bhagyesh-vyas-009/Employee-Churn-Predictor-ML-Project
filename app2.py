import streamlit as st
import pandas as pd
import pickle

pipe = pickle.load(open('pipeline1.pkl','rb'))

st.title('Employee Churn Predictor')
 
departments = ('sales', 'technical', 'support', 'IT', 'product_mng', 'marketing',
            'RandD', 'accounting', 'hr', 'management')
salaries = ('low','medium','high')


def show_prediction():
    p1 = float(e1)
    p2 = float(e2)
    p3 = float(e3)
    p4 = float(e4)
    p5 = float(e5)
    p6 = float(e6)
    p7 = float(e7)
    p8 = str(e8)
    p9 = str(e9)
    
    sample = pd.DataFrame({
        'satisfaction_level': [p1],
        'last_evaluation': [p2],
        'number_project': [p3],
        'average_montly_hours': [p4],
        'time_spend_company': [p5],
        'Work_accident': [p6],
        'promotion_last_5years': [p7],
        'departments': [p8],
        'salary': [p9]
    })
    result = pipe.predict(sample)
    if result == 1:
        st.write("An employee may leave the organization.")
    else:
        st.write("An employee may stay with the organization.")
    
        
e1 = st.slider("Employee satisfaction level", 0.0, 1.0, 0.5)
e2 = st.slider("Last evaluation score", 0.0, 1.0, 0.5)
e3 = st.slider("Number of projects assigned to", 1, 10, 5)
e4 = st.slider("Average monthly hours worked", 50, 300, 150)
e5 = st.slider("Time spent at the company", 1, 10, 3)
e6 = st.radio("Whether they have had a work accident", [0, 1])
e7 = st.radio("Whether they have had a promotion in the last 5 years", [0, 1])
e8 = st.selectbox("Department name", departments)
e9 = st.selectbox("Salary category", salaries)

if st.button("Predict"):
    show_prediction()
                
# if st.button("Predict"):
#     show_prediction()    
    
# def user_report():
#     satisfaction_level = st.slider("Employee satisfaction level", 0.0, 1.0, 0.5)
#     last_evaluation = st.slider("Last evaluation score", 0.0, 1.0, 0.5)
#     number_project = st.slider("Number of projects assigned to", 1, 10, 5)
#     average_montly_hours = st.slider("Average monthly hours worked", 50, 300, 150)
#     time_spend_company = st.slider("Time spent at the company", 1, 10, 3)
#     Work_accident = st.radio("Whether they have had a work accident", [0, 1])
#     promotion_last_5years = st.radio("Whether they have had a promotion in the last 5 years", [0, 1])
#     departments = st.selectbox("Department name", departments)
#     salary = st.selectbox("Salary category", salaries)

#     sample = pd.DataFrame({
#             'satisfaction_level': satisfaction_level,
#             'last_evaluation': last_evaluation,
#             'number_project': number_project,
#             'average_montly_hours': average_montly_hours,
#             'time_spend_company': time_spend_company,
#             'Work_accident': Work_accident,
#             'promotion_last_5years': promotion_last_5years,
#             'departments': departments,
#             'salary': salary
#         })
#     report_data=pd.DataFrame(sample)
#     return report_data

# user_data=user_report()
# result=pipe.predict(user_data)

#     report_data=pd.DataFrame(user_report,index=[0])
#     return report_data
#     e8 = 
    
