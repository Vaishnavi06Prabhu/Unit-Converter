import streamlit as st
from converter import convert_length, convert_weight, convert_temperature

st.title("🌐 Unit Converter")

menu = ["Length", "Weight", "Temperature"]
choice = st.sidebar.selectbox("Choose Conversion Type", menu)

if choice == "Length":
    st.header("Length Converter")
    units = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
    value = st.number_input("Enter value:", value=0.0)
    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif choice == "Weight":
    st.header("Weight Converter")
    units = ["milligram", "gram", "kilogram", "ounce", "pound"]
    value = st.number_input("Enter value:", value=0.0)
    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif choice == "Temperature":
    st.header("Temperature Converter")
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter value:", value=0.0)
    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
