def calculate_average():
    try:
        # Prompt the user to enter a list of numbers separated by spaces
        user_input = input("Enter a list of numbers separated by spaces: ")

        # Split the input string into a list of numbers
        number_strings = user_input.split()

        # Convert the list of strings to a list of floats
        numbers = [float(num) for num in number_strings]

        if not numbers:
            raise ValueError("The list is empty.")

        # Calculate the average of the numbers in the list
        average = sum(numbers) / len(numbers)

        # Display the calculated average
        print(f"The average of the numbers is: {average}")

    except ValueError as ve:
        # Handle non-numeric inputs or empty list
        print(f"Error: {ve}")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

    finally:
        # Display a goodbye message
        print("Goodbye!")


# Call the function to execute the program
calculate_average()
