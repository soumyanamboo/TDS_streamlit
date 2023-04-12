import streamlit as st

st.write("#App to find the largest of three numbres")
st.header('Enter three numbers: ')

def user_input():
  num1 = st.number_input("num1",min_value=0, max_value=100, step=1)
  num2 = st.number_input("num2",min_value=0, max_value=100, step=1)
  num3 = st.number_input("num3",min_value=0, max_value=100, step=1)
  if(num1 > num2):
    if(num1 > num3):
      largest = num1
    else:
      largest = num3
  else:
    if(num2 > num3):
      largest = num2
    else:
      largest = num3 
  st.write('The largest among the given 3 numbers is: ', largest)