from calculator import Calculator

admitted_operators = ['+', '-', '*', '**', 'pow', '/', '//', 'div', '%', 'mod', 'root', '√', 'break']

def main():
    
    while True:
        try:        
            operation = input("Your operation >>")
            if " " in operation:
                num1, operator, num2 = operation.split()
                
                num1 = float(num1)
                
                num2 = float(num2)

                output = Calculator(num1, num2)
                    
                
                if operator in admitted_operators:
                
                    if operator == '+':
                
                        print(output.add())
                
                    elif operator == '-':
                        print(output.sub())
                
                    elif operator == '*':
                
                        print(output.multiply())
                
                    elif operator == '**' or operator == 'pow':
                
                        print(output.power())
                
                    elif operator == 'root' or operator == '√':
                
                        print(output.root())
                
                    elif operator == '/':
                        print(output.div)       
                    
                    elif operator == '//' or operator == 'div':
                        print(output.integer_div)

                    elif operator == '%' or operator == 'mod':
                        print(output.mod())
                else:
                
                    print('Non valid operator :(, try again')
            
            elif "break" in operation:
                break
            
            else:
                print("The program works if you put a space between number and operation :)")

        except ValueError as v:
            print(v)
            print('Error: May you had type a string instead of a number')
            pass

    print('Thanks for use my calculator')


if __name__ == "__main__":
    print(""" 
    Calculator made by Daniel Diaz
    Instructions:
    1. Write tour operation in one line, with a space between 
        the numbers and the operators
    2. Accepted operations    
        -Normal operators.
        + for add
        - for substract
        * for multiply
        / for normal division
        - Special operators:
        pow or ** for power
        // or div for integer division
        % or mod for module
        root or √ for root
    Note: for root the first number represents the 
    index exponent and the second the radical argument.
    3. If you want to exit type 'break', without quotes
    """)

    main()
