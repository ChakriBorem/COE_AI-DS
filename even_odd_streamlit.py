import streamlit as st
st.title("Even or Odd")
num = st.number_input("Enter your basic salary:", min_value=0, step=1)
if st.button("Even or Odd"):
    if num % 2 == 0:
        st.success("Even number")
    else:
        st.success("Odd number")
        