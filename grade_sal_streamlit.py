import streamlit as st
p = st.number_input("Enter Project marks:", min_value=0, step=1)
st.title("Grade Calculator")
i = st.number_input("Enter Internal marks:", min_value=0, step=1)
e = st.number_input("Enter External marks:", min_value=0, step=1)
if st.button("Calculate Grade"):
    if p >= 50 and i >= 50 and e >= 50:
        total = (p * 0.7) + (i * 0.1) + (e * 0.2)
        if total > 90:
            st.success("A grade")
        elif total > 80:
            st.success("B grade")
        else:
            st.success("C grade")
    else:
        if p < 50:
            st.success(f"Failed in project and score is {p}")
        if i < 50:
            st.success(f"Failed in internal and score is {i}")
        if e < 50:
            st.success(f"Failed in external and score is {e}")
            