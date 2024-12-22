import streamlit as st
st.title("Gross Salary Calculator")
bsal = st.number_input("Enter your basic salary:", min_value=0, step=500)
if st.button("Calculate Gross Salary"):
    hra = 0
    da = 0
    if bsal < 10000:
        hra = 0.67 * bsal
        da = 0.73 * bsal
    elif bsal < 20000:
        hra = 0.69 * bsal
        da = 0.76 * bsal
    else:
        hra = 0.73 * bsal
        da = 0.89 * bsal
    gs = hra + da + bsal
    st.success(gs)
    