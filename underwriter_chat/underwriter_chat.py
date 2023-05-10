import streamlit as st
import pandas as pd


def main():
    st.title("Insurance Chatbot")

    # Get user input
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        # Send user input to ChatGPT
        #bot_response = "Hi what can i do for you today"
        a = st.success("Hi what can i do for you today")
    st.markdown("---")
    if a:
        user_input1 = st.text_input("You", "")
        if st.button("send"):

            st.success("Data Analytics Software \
                        Predictive Modeling Tools \
                        Risk Assessment Software \
                        Underwriting Rules Engines \
                        Document Management Systems \
                        Data visualization tools \
                        Fraud detection tools")
            if b:
                user_input2 = st.text_input("You:", "")
                if st.button("send"):
                        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
                        if uploaded_file:
                                # Process the uploaded CSV file
                            df = pd.read_csv(uploaded_file)
                                # Perform predictions or other operations on the data
                                # Display the results using st.write() or st.table()
                            st.write(df.head())  # Example: Display the first few rows of the uploaded file

if __name__ == "__main__":
    main()

