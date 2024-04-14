while True:
    try:
        original_serving_amount = input("Enter the original serving amount in your recipe: ")
        desired_serving_amount = input("Enter the desired serving amount you would like to prepare: ")

        # Convert the input strings to integers
        original_serving_amount = int(original_serving_amount)
        desired_serving_amount = int(desired_serving_amount)

        # Calculate the adjustment factor
        adjusted_amount = desired_serving_amount / original_serving_amount
        print(f"Your amount is: {adjusted_amount}")
        break  # Exit the loop if everything went well

    except ValueError:
        print("Please enter valid numbers for servings. Try again.")
    except ZeroDivisionError:
        print("Serving amount cannot be zero. Try again.")
    finally:
        print("Enjoy and thanks for cooking with python!")
