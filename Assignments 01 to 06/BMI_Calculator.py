import streamlit as st

# Title of the app
st.title("🚀 Advanced BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and understand your weight status.")

# Customizable units
unit_system = st.radio("Select your unit system:", ("Metric (kg, meters)", "Imperial (pounds, feet/inches)"))

# Input fields based on unit system
if unit_system == "Metric (kg, meters)":
    weight = st.slider("Enter your weight (in kg)", 30.0, 200.0, 70.0)
    height = st.slider("Enter your height (in meters)", 1.0, 2.5, 1.75)
else:
    weight = st.slider("Enter your weight (in pounds)", 66.0, 440.0, 150.0)
    feet = st.slider("Enter your height (feet)", 3, 8, 5)
    inches = st.slider("Enter your height (inches)", 0, 11, 9)
    height = (feet * 12 + inches) * 0.0254  # Convert feet/inches to meters
    weight = weight * 0.453592  # Convert pounds to kg

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # BMI Categories with visual feedback
    st.subheader("BMI Category")
    if bmi < 18.5:
        st.error("Underweight 🏋️‍♂️ - You need to gain weight.")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal Weight ✅ - You're in a healthy range!")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight ⚠️ - You need to lose some weight.")
    else:
        st.error("Obese 🚨 - You need to take action to improve your health.")

    # BMI Progress Bar
    st.subheader("BMI Progress Bar")
    progress = (bmi - 10) / 30  # Scale BMI from 10 to 40 for progress bar
    st.progress(progress)

    # Weight Status Tracker
    st.subheader("Weight Status")
    ideal_low = 18.5 * (height ** 2)
    ideal_high = 24.9 * (height ** 2)
    if bmi < 18.5:
        st.write(f"To reach a normal weight, you need to gain **{(ideal_low - weight):.2f} kg**.")
    elif bmi > 24.9:
        st.write(f"To reach a normal weight, you need to lose **{(weight - ideal_high):.2f} kg**.")
    else:
        st.write("You're already in the ideal weight range. Keep it up! 💪")

    # Save Results
    st.subheader("Save Your Results")
    result_text = f"Weight: {weight:.2f} kg\nHeight: {height:.2f} meters\nBMI: {bmi:.2f}\nCategory: "
    if bmi < 18.5:
        result_text += "Underweight"
    elif 18.5 <= bmi < 24.9:
        result_text += "Normal Weight"
    elif 25 <= bmi < 29.9:
        result_text += "Overweight"
    else:
        result_text += "Obese"
    
    st.download_button(
        label="Download BMI Results",
        data=result_text,
        file_name="bmi_results.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.write("Made with ❤️ by [Your Name]")
