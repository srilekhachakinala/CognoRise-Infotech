while True:
    def calculate():
        print("Welcome to the Enchanted Realm of Calculations")

        print("I'm here to assist you with arthimetic quests")

        num1 = float(input("Tell me the first number you seek: "))
        
        print("choose the operation  you like to perform?")
        print("1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (×)")
        print("4: Division (÷)")
        
        operation = input("Please enter the number corresponding to the operation: ")
        
        
        while operation not in ['1', '2', '3', '4']:
            print("Oops! you had selected a invalid choice. Please try again.")
            operation = input("Please enter the number corresponding to the operation: ")
        
        num2 = float(input("Please enter the second number: "))
        if operation == '1':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == '2':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == '3':
            result = num1 * num2
            operation_symbol = '×'
        elif operation == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result=num1/num2
                operation_symbol='/'
        print(f"\n{num1} {operation_symbol} {num2} = {result}")
        
    calculate()
    choice=input("Do You want to perform the calculation again Yes or No?")
    if choice!='Yes':
            print("Thanks for using the enhanced realm of calculations. Have a great day!")

            break