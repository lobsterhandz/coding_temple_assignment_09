def convert_fahrenheit_to_celsius(fahrenheit):
    try:
        # Conversion formula
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except ValueError:
        print("Not a number.")
    finally:
        print("Conversion attempted.")  # This message is more for debugging; actual user experience enhancement happens outside this function.

# Main loop for user input
while True:
    user_input = input("Enter temperature in Fahrenheit (or 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Thank you for using the weather forecast application. Have a great day!")  # Thanking the user when they decide to exit.
        break

    try:
        temperature_fahrenheit = float(user_input)
        temperature_celsius = convert_fahrenheit_to_celsius(temperature_fahrenheit)
        print(f"{temperature_fahrenheit} Fahrenheit is {temperature_celsius:.2f} Celsius.")  # User-friendly formatted output
    except ValueError:
        print("Please enter a valid number.")
    finally:
        # Thank the user after each conversion attempt, regardless of the outcome
        print("Thank you for using the weather forecast application. Feel free to convert another temperature.")
