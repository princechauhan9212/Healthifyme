import os
import pandas as pd
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
# Lets get the api key from the environment
gemini_api_key = os.getenv('Google_API_Key_1')

# Lets configure the model

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite',
                               api_key=gemini_api_key)

# Design the UI of application
st.title(":orange[HealthifyMe:]  Your Personal Health Assistant")
st.markdown('''
            This application will assist you to get better and customized 
            Health asvice. You can ask related issues and get teh personalized guidance''')
st.write('''
Follow These steps :
* Enter your details  in sidebar
* Rate your activity and fitness on the scale of 0-5.
* submit your details
* Ask your qyestion on the main page .
* click on generate and relax.''')



# Lets design the sidebar for all the user parameters
st.sidebar.header(':red[Enter Your Details]')

name = st.sidebar.text_input('Enterr your Name :')
gender = st.sidebar.selectbox('Enter your Gender',['Male','Female'])
age = st.sidebar.text_input('Enter your age ')

weight = st.sidebar.text_input('Enter your weight in Kgs')

height = st.sidebar.text_input('Enter your height in cms')

bmi = pd.to_numeric(weight)/((pd.to_numeric(height)/100)**2)


active = st.sidebar.slider('Rate your activity (0-5)',0,5,step=1)
fitness = st.sidebar.slider('Rate your fitness (0-5)',0,5,step=1)
if st.sidebar.button('Submit'):
    st.sidebar.write(f"{name}, Your BMI is : {bmi} Kg/m^2")

# Lets use the gemini model to generate the report 

user_input = st.text_input('ask me your question')
prompt = f'''
<Role> your are expert in in health and wellness and has 10+ years experience in guiding people 
<Goal> generate the customized report addressing the problem the user has asked 
<context> Here ar ethe details thath the user has provided 
name = {name}
age = {age}
gender = {gender}
height = {height}
weight = {weight}
bmi = {bmi}
activity rating (0-5) = {active}
fitness rating (0-5) = {fitness}


<format> * following should be outline of the report ,in the sequence provided 
* start with the 2-3 line of comment on the details thath user has been provided
* explain what the real problem could be on the basis of input the user has provided 
* suggest the possible reasong for the problem 
* what are the possible solutions.
* mention the doctor from which specialization can be visited if required 
* mention any change in the diet whcih is required.
* In the laste create final summary of all the things thath has been discussed in the report


<Instructions>
*use bullet points where ever possible.
* Create tables to represent any data where ever possible.
*strictly don not advice any medicine . '''

if st.button('Generate'):
    response = model.invoke(prompt)
    st.write(response.content)

