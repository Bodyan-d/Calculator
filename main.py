import math

# This is a simple calculator that can perform basic operations

list_to_calculate = []
EXITING_LABEL = "Exiting..."    

def main(): 
    is_running = True
    print("-------------------------")
    print("Welcome to the calculator")
    print("_________________________")
    print()
    
    # Main loop
    while is_running:
        user_number = input("Enter a number (x to exit): ").strip()
        print()
        
        if user_number.lower() == "x":
            is_running = False
            print(EXITING_LABEL)
            clear_list()
            break
        elif not user_number.isnumeric():
            print("You entered: ",  user_number)
            print("Please enter a valid number")
            continue
        list_to_calculate.append(user_number)
        show_expression()
        calculate()
        


def calculate():
    is_calculating = False
    
    # Loop for calculating the expression
    while not is_calculating:
        
        user_method = input("Enter a method (pow, dew, mult, add, subtr) or num (calc to calculate)(x to exit): ")
        print()        
        if handle_exit(user_method):
            is_calculating = True
            print(EXITING_LABEL)
            clear_list()
            break
        
        if user_method.lower() == "calc":
            print("Calculating...")
            calculate_expression()
            is_calculating = True
            break
        
        handle_method(user_method)
        show_expression()
       


def handle_exit(user_method):
    if user_method.lower() == "x":
        print(EXITING_LABEL)
        clear_list()
        return True
    return False

def handle_method(user_method):
    
    if list_to_calculate[-1] in ["**", "/", "*", "+", "-"] and not user_method.isnumeric():
        print("Please enter a number")
        return
    if list_to_calculate[-1].isnumeric() and user_method.isnumeric():
        print("Please enter a method")  
        return     

    if user_method.isnumeric():
        list_to_calculate.append(user_method)
    else:
        method_dict = {
            "pow": "**",
            "dew": "/",
            "mult": "*",
            "add": "+",
            "subtr": "-"
        }
        if user_method.lower() in method_dict:
            list_to_calculate.append(method_dict[user_method.lower()])
        else:
            print("Please enter a valid method dude")

def calculate_expression(): 
    try:
        to_calculate = "".join(list_to_calculate)
        print("Result :", eval(to_calculate))
        clear_list()
    except ZeroDivisionError:
        print("Cannot divide by zero")
        clear_list()
    except SyntaxError:
        print("Please enter a valid expression")
        clear_list()
    except Exception as e:
        print("An error occured: ", e)
        clear_list()
    
def clear_list():
    list_to_calculate.clear()
    
def show_expression():
    print("-------------------------")
    print("".join(list_to_calculate))
    print("-------------------------")
  

if __name__ == "__main__":
    main()