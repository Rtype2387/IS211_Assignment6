import unittest
from conversions import (convertCelsiusToKelvin, convertCelsiusToFahrenheit,
                         convertFahrenheitToCelsius, convertFahrenheitToKelvin,
                         convertKelvinToCelsius, convertKelvinToFahrenheit)

from conversions_refactored import convert, ConversionNotPossible

class TestTemperatureConversions(unittest.TestCase):
    def test_celsius_to_kelvin(self):
        print("Testing 0 C to Kelvin")
        self.assertAlmostEqual(convertCelsiusToKelvin(0.0), 273.15)

        print("Testing 100 C to Kelvin")
        self.assertAlmostEqual(convertCelsiusToKelvin(100.0), 373.15)

        print("Testing 300 C to Kelvin")
        self.assertAlmostEqual(convertCelsiusToKelvin(300.0), 573.15)

        print("Testing -40 C to Kelvin")
        self.assertAlmostEqual(convertCelsiusToKelvin(-40.0), 233.15)

        print("Testing 37 C to Kelvin")
        self.assertAlmostEqual(convertCelsiusToKelvin(37.0), 310.15)

    def test_celsius_to_fahrenheit(self):
        print("Testing 0 C to Fahrenheit")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0.0), 32.0)

        print("Testing 100 C to Fahrenheit")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100.0), 212.0)

        print("Testing 300 C to Fahrenheit")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300.0), 572.0)

        print("Testing -40 C to Fahrenheit")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40.0), -40.0)

        print("Testing 37 C to Fahrenheit")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(37.0), 98.6)

    def test_fahrenheit_to_celsius(self):
        print("Testing 32 F to Celsius")
        self.assertAlmostEqual(convertFahrenheitToCelsius(32.0), 0.0)

        print("Testing 212 F to Celsius")
        self.assertAlmostEqual(convertFahrenheitToCelsius(212.0), 100.0)

        print("Testing -40 F to Celsius")
        self.assertAlmostEqual(convertFahrenheitToCelsius(-40.0), -40.0)

        print("Testing 572 F to Celsius")
        self.assertAlmostEqual(convertFahrenheitToCelsius(572.0), 300.0)

        print("Testing 98.6 F to Celsius")
        self.assertAlmostEqual(convertFahrenheitToCelsius(98.6), 37.0)

    def test_fahrenheit_to_kelvin(self):
        print("Testing 32 F to Kelvin")
        self.assertAlmostEqual(convertFahrenheitToKelvin(32.0), 273.15)

        print("Testing 212 F to Kelvin")
        self.assertAlmostEqual(convertFahrenheitToKelvin(212.0), 373.15)

        print("Testing -40 F to Kelvin")
        self.assertAlmostEqual(convertFahrenheitToKelvin(-40.0), 233.15)

        print("Testing 572 F to Kelvin")
        self.assertAlmostEqual(convertFahrenheitToKelvin(572.0), 573.15)

        print("Testing 98.6 F to Kelvin")
        self.assertAlmostEqual(convertFahrenheitToKelvin(98.6), 310.15)

    def test_kelvin_to_celsius(self):
        print("Testing 273.15 K to Celsius")
        self.assertAlmostEqual(convertKelvinToCelsius(273.15), 0.0)

        print("Testing 373.15 K to Celsius")
        self.assertAlmostEqual(convertKelvinToCelsius(373.15), 100.0)

        print("Testing 233.15 K to Celsius")
        self.assertAlmostEqual(convertKelvinToCelsius(233.15), -40.0)

        print("Testing 573.15 K to Celsius")
        self.assertAlmostEqual(convertKelvinToCelsius(573.15), 300.0)

        print("Testing 310.15 K to Celsius")
        self.assertAlmostEqual(convertKelvinToCelsius(310.15), 37.0)

    def test_kelvin_to_fahrenheit(self):
        print("Testing 273.15 K to Fahrenheit")
        self.assertAlmostEqual(convertKelvinToFahrenheit(273.15), 32.0)

        print("Testing 373.15 K to Fahrenheit")
        self.assertAlmostEqual(convertKelvinToFahrenheit(373.15), 212.0)

        print("Testing 233.15 K to Fahrenheit")
        self.assertAlmostEqual(convertKelvinToFahrenheit(233.15), -40.0)

        print("Testing 573.15 K to Fahrenheit")
        self.assertAlmostEqual(convertKelvinToFahrenheit(573.15), 572.0)

        print("Testing 310.15 K to Fahrenheit")
        self.assertAlmostEqual(convertKelvinToFahrenheit(310.15), 98.6)

class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(convert("Celsius", "Fahrenheit", 0.0), 32.0)
        self.assertAlmostEqual(convert("Celsius", "Kelvin", 0.0), 273.15)

        self.assertAlmostEqual(convert("Fahrenheit", "Celsius", 32.0), 0.0)
        self.assertAlmostEqual(convert("Fahrenheit", "Kelvin", 32.0), 273.15)

        self.assertAlmostEqual(convert("Kelvin", "Celsius", 273.15), 0.0)
        self.assertAlmostEqual(convert("Kelvin", "Fahrenheit", 273.15), 32.0)

    def test_distance_conversions(self):
        self.assertAlmostEqual(convert("Miles", "Yards", 1.0), 1760.0)
        self.assertAlmostEqual(convert("Miles", "Meters", 1.0), 1609.344)

        self.assertAlmostEqual(convert("Yards", "Miles", 1760.0), 1.0)
        self.assertAlmostEqual(convert("Yards", "Meters", 1.0), 0.9144)

        self.assertAlmostEqual(convert("Meters", "Miles", 1609.344), 1.0)
        self.assertAlmostEqual(convert("Meters", "Yards", 0.9144), 1.0)

    def test_same_unit(self):
        self.assertAlmostEqual(convert("Celsius", "Celsius", 25.0), 25.0)
        self.assertAlmostEqual(convert("Fahrenheit", "Fahrenheit", 75.0), 75.0)
        self.assertAlmostEqual(convert("Kelvin", "Kelvin", 300.0), 300.0)

        self.assertAlmostEqual(convert("Miles", "Miles", 5.0), 5.0)
        self.assertAlmostEqual(convert("Yards", "Yards", 10.0), 10.0)
        self.assertAlmostEqual(convert("Meters", "Meters", 20.0), 20.0)

    def test_incompatible_units(self):
        self.assertRaises(
            ConversionNotPossible,
            convert,
            "Celsius",
            "Meters",
            10.0
        )
if __name__ == "__main__":
    unittest.main()
