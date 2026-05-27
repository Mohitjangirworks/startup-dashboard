import streamlit as st
import pandas as pd
import  time

st.title('Startup Dashboard')
st.header('Header')
st.subheader('Sub Header')
#
# streamlit run App.py

st.write("this is para")
st.markdown(
    '''
    ### This is my markdown
    - a
    -b
    '''
)


st.code('''
function(){
   return a+b;
}
''')

st.latex('x^2+Y^2')

#Display

df=pd.DataFrame({
    'Name':['Mohit','Ankit'],
    'Marks':[44,55],
    'Percentage':[55,75]
})
st.dataframe(df)

st.metric('Revenue','3Lakh', '-3%')

st.json(
    {
        'Name': ['Mohit', 'Ankit'],
        'Marks': [44, 55],
        'Percentage': [55, 75]
    }
)

st.image('Mohit.png')

#creating Layout
st.sidebar.title('Sidebar ka title')

col1,col2=st.columns(2)
with col1:
    st.image('Mohit.png')
with col2:
    st.image('Mohit.png')


st.error("Login Failed")
st.success("Login Successfull")


# bar =st.progress(0)
# for i in range (1,100):
#     time.sleep(0.1)
#     bar.progress(i)

email=st.text_input("Enter your Email")
number=st.number_input('Enter Your Age')
st.date_input("Enter Registration Date")


#
# --------------------------

import streamlit as st
st.title('Registration Form')
email=st.text_input("Enter Your Mail-ID")
password=st.text_input("Enter Your Pass")

gender=st.selectbox('Select the gender',['Male','Female','Others'])

btn=st.button('Login')
if btn:
    if email == 'mohit@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
        #st.success("Login Successfull")
    else:
        st.error("Login Failed")





import streamlit as st

st.sidebar.title("side bar ")

st.title('Registration Form')
email=st.text_input("Enter Your Mail-ID")
password=st.text_input("Enter Your Pass")

gender=st.selectbox('Select the gender',['Male','Female','Others'])

btn=st.button('Login')
if btn:
    if email == 'mohit@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
        #st.success("Login Successfull")
    else:
        st.error("Login Failed")



import streamlit as st
import pandas as pd

file=st.file_uploader("Upload a csv file")

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.mean())