import streamlit as st
st.title("Expenditure Percentage")
sal = st.number_input("Enter Employee salary:", min_value=0, step=500)
b1 = st.number_input("Enter bill 1 amount", min_value=0, step=100)
b2 = st.number_input("Enter bill 2 amount", min_value=0, step=100)
b3 = st.number_input("Enter bill 3 amount", min_value=0, step=100)
if st.button("Calculate"):
    b = b1 + b2 + b3
    res = (b / sal) * 100
    st.success(f"The percentage of salary used for shopping is {res}")
