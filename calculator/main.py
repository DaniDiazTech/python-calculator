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

admitted_operators = ['+', '-', '*', '**', 'pow', '/', '//', 'div', '%', 'mod', 'root', '√', 'break']


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def power(x, y):
    return x ** y


def div(x, y):
    return x / y


def integer_div(x, y):
    return x // y


def mod(x, y):
    return x % y


def root(x, y):
    return y ** (1 / x)


while True:
    operation = input("Your operation >>")
    if " " in operation:
        num1, operator, num2 = operation.split()
        num1 = float(num1)
        num2 = float(num2)
        if operator in admitted_operators:
            if operator == '+':
                print(add(num1, num2))
            elif operator == '-':
                print(sub(num1, num2))
            elif operator == '*':
                print(multiply(num1, num2))
            elif operator == '**' or operator == 'pow':
                print(power(num1, num2))
            elif operator == 'root' or operator == '√':
                print(root(num1, num2))
            elif operator == '/':
                if num2 != 0:
                    print(div(num1, num2))
                else:
                    print('Error: Division by cero, try again')
            elif operator == '//' or operator == 'div':
                if num2 != 0:
                    print(integer_div(num1, num2))
                else:
                    print('Error: Integer division by cero, try again')
            elif operator == '%' or operator == 'mod':
                if num2 != 0:
                    print(mod(num1, num2))
                else:
                    print('Error: Integer division by cero, try again')
        else:
            print('Non valid operator :(, try again')
    elif "break" in operation:
        break
    else:
        print("The program works if you put a space between number and operation :)")

print('Thanks for use my calculator')


    
    
    
    
