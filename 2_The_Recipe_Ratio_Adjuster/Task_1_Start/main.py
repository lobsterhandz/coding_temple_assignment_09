while True:
    try:
        original_serving_amount = input("Enter the original serving amount in your recipe: ")
        desired_serving_amount = input("Enter the desired serving amount you would like to prepare: ")    
    
    except ValueError:
        print("Please enter valid numbers for servings. Try again.")

