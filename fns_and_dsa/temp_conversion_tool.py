FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
    
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

try:
    temp_input = float(input("Enter the temperature to convert: "))
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit_input == 'F':
        converted_value = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {converted_value}°C")
    elif unit_input == 'C':
        converted_value = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {converted_value}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
