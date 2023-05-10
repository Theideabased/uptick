import streamlit as st
import pandas as pd

def main():
    st.title("Odaibo Underwriting chatbot")
    st.write("Building efficiency and accuracy in Underwriting") 
    name = st.text_input("Enter your name:")
    
    if name:
        st.write(f"Hello, {name}!")
        result = st.text_input("You: ")
        
        if result:
            st.write("Data Analytics Software, Predictive Modeling Tools, Risk Assessment Software, Underwriting Rules Engines , Document Management Systems, Data visualization tools, Fraud detection tools ")
            st.text_input("You:")
            uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
            if uploaded_file:

                df = pd.read_csv(uploaded_file)
                                # Perform predictions or other operations on the data
                                # Display the results using st.write() or st.table()
                st.write(df.head())
                input_3 = st.text_input("what do you want to do with the data:")
                
                if input_3:
                    formula = "5.2391 + (0.1773 * X2^1) + (-0.0002 * X3^1)"
                    st.write(f"Model is {formula}")
                    last_input = st.text_input ("You")
                    if last_input:
                        st.write("This is a polynomial model")
if __name__ == '__main__':
    main()
