# Simple Arithmetic Calculator 

def calculator():
    print("Enter your arithmetic operation (e.g., 5 + 3, 10 / 2):")
    
    try:
        # Take input from the user
        operation = input("Operation: ")
        
        # Evaluate the expression using eval
        result = eval(operation)
        
        # Display result
        print(f"The result is: {result}")
        
    except ZeroDivisionError:
        print("Error! Division by zero.")
    except Exception as e:
        print(f"Invalid input! {e}")

# Run the calculator
calculator()
