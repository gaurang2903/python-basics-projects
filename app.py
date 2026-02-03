import streamlit as st

st.title("Leap Year Detection App")

year = st.number_input("Enter a year", min_value=1, step=1)

if st.button("Check"):
    if year % 400 == 0:
        st.success(f"{year} is a Leap Year")
    else:
        if year % 100 == 0:
            st.error(f"{year} is NOT a Leap Year")
        else:
            if year % 4 == 0:
                st.success(f"{year} is a Leap Year")
            else:
                st.error(f"{year} is NOT a Leap Year")
