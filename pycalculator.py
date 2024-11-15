## Made On Kali Linux

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# For Stopping user from dividing a number by 0 and crashing the terminal we user if and return function

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to this goddamn calculator!")
    
    while True:
        print("$Select operation:")
        print("1.Press 1 to Add")
        print("2.Press 2 to Subtract")
        print("3.Press 3 to Multiply")
        print("4.Press 4 to Divide")
        print("5.Press 5 to Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        elif choice == '5':
            print("Exiting the Calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    calculator()
