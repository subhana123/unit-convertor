import streamlit as st

# Dictionary of conversion factors
conversion_factors = {
    "Length": {
        "meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084, "inches": 39.3701
    },
    "Weight": {
        "kilograms": 1, "grams": 1000, "pounds": 2.20462, "ounces": 35.274
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    },
    "Time": {
        "seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400
    },
    "Area": {
        "square meters": 1, "square kilometers": 1e-6, "square miles": 3.861e-7, "square feet": 10.764
    },
    "Volume": {
        "liters": 1, "milliliters": 1000, "cubic meters": 0.001, "gallons": 0.264172
    }
}

# Function to handle unit conversion
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value  # Same unit
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Streamlit UI
st.title("🌍 Universal Unit Converter")
st.write("Convert between different units easily!")

# Select Category
category = st.selectbox("Choose a category:", list(conversion_factors.keys()))

# Select Units
from_unit = st.selectbox("From:", list(conversion_factors[category].keys()))
to_unit = st.selectbox("To:", list(conversion_factors[category].keys()))

# Enter Value
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

# Conversion Button
if st.button("Convert"):
    if from_unit == to_unit:
        st.warning("Please select different units for conversion.")
    else:
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
