
class Calculator:

    def __init__(self, x, y):
       self.x = x
       self.y = y 

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def power(self):
        return self.x ** self.y

    def div(self):
        if self.y != 0: 
            return self.x / self.y

        else:
            
            return 'Error: Division by cero, try again'

    def integer_div(self):
        if self.y != 0:
            return self.x // self.y
        else:
            return 'Error: Integer division by cero, try again'

    def mod(self):
        if self.y != 0:
            return self.x % self.y
        else:
            return 'Error: modulo operation by cero, try again'

    def root(self):
        return self.y ** (1 / self.x)

if __name__ == "__main__":
    print('This is a module where a wrote the class I used to implement the calculator, I think it is not useful to use it')
    
    pass