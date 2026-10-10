class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    value = float(value)

    if fromUnit == toUnit:
        return float(value)

    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    distance_units = ["Miles", "Yards", "Meters"]

    if fromUnit in temperature_units and toUnit in temperature_units:

        if fromUnit == "Celsius" and toUnit == "Fahrenheit":
            return (value * 9 / 5) + 32

        elif fromUnit == "Celsius" and toUnit == "Kelvin":
            return value + 273.15

        elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
            return (value - 32) * 5 / 9

        elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
            return (value - 32) * 5 / 9 + 273.15

        elif fromUnit == "Kelvin" and toUnit == "Celsius":
            return value - 273.15

        elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
            return (value - 273.15) * 9 / 5 + 32

    elif fromUnit in distance_units and toUnit in distance_units:

        if fromUnit == "Miles" and toUnit == "Yards":
            return value * 1760

        elif fromUnit == "Miles" and toUnit == "Meters":
            return value * 1609.344

        elif fromUnit == "Yards" and toUnit == "Miles":
            return value / 1760

        elif fromUnit == "Yards" and toUnit == "Meters":
            return value * 0.9144

        elif fromUnit == "Meters" and toUnit == "Miles":
            return value / 1609.344

        elif fromUnit == "Meters" and toUnit == "Yards":
            return value / 0.9144

    else:
        raise ConversionNotPossible("These units cannot be converted")