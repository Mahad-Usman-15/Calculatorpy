import streamlit as st;
st.title("Calculator")
st.write("Number1")
inputfromuser =st.number_input("Enter the first number",value=0)
st.write("Number2")
inputfromuser2 =st.number_input("Enter the second number",value=0)
st.write("Operator")
operator=st.selectbox("Select the operator",["+","-","*","/"])

if operator=="+":
    result=inputfromuser+inputfromuser2
    st.success(f"Result:{result}")
elif operator=="-":
    result=inputfromuser-inputfromuser2
    st.success(f"Result:{result}")
elif operator=="*":
    result=inputfromuser*inputfromuser2
    st.success(f"Result:{result}")
elif operator=="/":
    if inputfromuser2>0 and inputfromuser:
        result=inputfromuser/inputfromuser2
        st.success(f"Result:{result}")
    else:
        st.success("Enter value greater than zero")
else:
  st.error("Invalid input")      
