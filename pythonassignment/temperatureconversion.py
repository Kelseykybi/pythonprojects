class Temperature:
    def convertFahrenheit(self, celsius):
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        
    def convertCelsius(self, fahrenheit):
        # Convert Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")

# Example usage
temp = Temperature()
temp.convertFahrenheit(25)  # Convert 25°C to Fahrenheit
temp.convertCelsius(77)     # Convert 77°F to Celsius
