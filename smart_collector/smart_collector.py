import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib
from pathlib import Path

# load the dataset
car_insurance_csv = Path(__file__).parents[1] /'smart_collector/car_insurance.csv'
data = pd.read_csv(car_insurance_csv)
# Load the model
my_pipeline = joblib.load(open('insurance_june_2023.pkl',"rb")) 
# Define the app
def app():
    st.title('Smart collector')
    st.write('input your car details and get your policy:')
    
    # Create input widgets for each feature
    manufacturer = st.selectbox("manufacturer", options=(list( data['Manufacturer'].unique())))
    model = st.selectbox("Model", options=(list( data['Model'].unique())))
    mileage = st.number_input('Mileage')
    engine_volume = st.slider('Engine Volume', min_value=1, max_value=6, step=1)
    airbags = st.slider('airbags', min_value=1, max_value=15, step=1)
    category = st.selectbox("Category", options =(data['Category'].unique()))
    prod_yr = st.selectbox("production year", options=(list( data['Prod. year'].unique())))
    # set your values
    df_from_input = pd.DataFrame([{
   'Manufacturer' : manufacturer,
   'Model': model,
   'Category': category,
   'Mileage': mileage,
   'Prod. year': prod_yr,
   'Engine volume': engine_volume,
   'Airbags': airbags,
  }])

    #price = model.predict(df_from_input)
    #return price

    # Display the predicted price to the user
    if st.button('Submit'):
        price = my_pipeline.predict(df_from_input)
        st.success(f'your policy is {price[0]*10:,.2f} naira.')
        if price >= 1000000:
            st.write('this vechicle has a high risk and it is unacceptable')
        elif price >= 500000:
            st.write('this vechicle has a high risk but it is acceptable')
        else:
            st.write('this vechicle has a low risk')

    
if __name__ == '__main__':
    app()
