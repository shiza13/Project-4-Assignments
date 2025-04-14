import streamlit as st

# Set the title of the web app
st.title("BMI Calculator")

# Instructions
st.write("This is a simple BMI Calculator. Please enter your height and weight.")

# Create input fields for height and weight
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm)", min_value=1.0, step=0.1)

# Calculate BMI when both fields are filled
if weight > 0 and height > 0:
    # Convert height from cm to meters
    height_in_meters = height / 100
    # Calculate BMI
    bmi = weight / (height_in_meters ** 2)
    
    # Display the result
    st.write(f"Your BMI is: {bmi:.2f}")

    # Provide the BMI category
    if bmi < 18.5:
        st.write("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obesity")
else:
    st.write("Please enter valid values for weight and height.")
