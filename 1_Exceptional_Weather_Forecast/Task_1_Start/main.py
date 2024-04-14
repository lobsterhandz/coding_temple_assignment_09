# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

while True:
    try:
        temperature_fahrenheit = input("Please enter the temperature in Fahrenheit (or type 'exit' to quit): ")
        
        if temperature_fahrenheit.lower() == 'exit':
            break

        temperature_fahrenheit = float(temperature_fahrenheit)
        
        print(f"You entered: {temperature_fahrenheit} Fahrenheit")
        
    except ValueError:
        print("Sorry, that's not a valid number. Please try again.")
