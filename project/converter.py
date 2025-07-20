
# Length Conversion Factors (to meter)
length_factors = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34,
}

# Weight Conversion Factors (to kilogram)
weight_factors = {
    "milligram": 0.000001,
    "gram": 0.001,
    "kilogram": 1,
    "ounce": 0.0283495,
    "pound": 0.453592,
}

# ------------------------

def convert_length(value, from_unit, to_unit):
    value_in_meters = value * length_factors[from_unit]
    result = value_in_meters / length_factors[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    value_in_kg = value * weight_factors[from_unit]
    result = value_in_kg / weight_factors[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    # Convert input to Celsius first
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15

    # Convert Celsius to target
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
