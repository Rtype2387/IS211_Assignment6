
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    kelvins = (fahrenheit - 32) * 5 / 9 + 273.15
    return kelvins


def convertKelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return fahrenheit