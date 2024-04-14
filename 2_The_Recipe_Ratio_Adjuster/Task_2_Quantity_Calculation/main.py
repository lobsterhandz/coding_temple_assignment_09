while True:
    try:
        original_serving_amount = input("Enter the original serving amount in your recipe: ")
        desired_serving_amount = input("Enter the desired serving amount you would like to prepare: ")

        # Convert the input strings to integers
        original_serving_amount = int(original_serving_amount)
        desired_serving_amount = int(desired_serving_amount)
        adjusted_amount = desired_serving_amount / original_serving_amount
       
    except ValueError:
        print("Please enter valid numbers for servings. Try again.")
    except ZeroDivisionError:
        print("Original serving amount cannot be zero. Try again.")
