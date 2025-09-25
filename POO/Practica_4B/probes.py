class Calculator:
    """
    A simple calculator class that can perform a sequence of operations
    on a running total.
    """

    def __init__(self, initial_value=0):
        """
        Initializes the calculator with a starting value.
        """
        self.total = initial_value

    def add(self, number):
        """Adds a number to the current total."""
        self.total += number
        return self  # This returns the instance, allowing for method chaining

    def subtract(self, number):
        """Subtracts a number from the current total."""
        self.total -= number
        return self

    def multiply(self, number):
        """Multiplies the current total by a number."""
        self.total *= number
        return self

    def divide(self, number):
        """Divides the current total by a number."""
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        
        self.total /= number
        return self

    def power(self, number):
        """Raises the current total to the power of a number."""
        self.total **= number
        return self
    
    def get_total(self):
        """Returns the current total."""
        return self.total
    
    def clear(self):
        """Resets the total to zero."""
        self.total = 0
        return self


def main():
    print('Welcome to the calculator!!')
    
    while True:
        option = input('exit or operation: ')
        
        if option == 'exit':
            print('see you later!!')
            break
    
        num1_entry = input('Number: ')
        num1 = float(num1_entry)
        
        calc = Calculator(num1)
     
        i = 0
        while True:
            message = 'Operation(+, -, *, /, ^): '
            
            if i > 0:
                message = 'Operation(+, -, *, /, ^) or result: '
            
            i += 1
            
            operation = input(message)
            
            if operation == 'result':
                print(f'result: {calc.get_total()}\n')
                calc.clear()
                break
            
            num2_entry = input('Number: ')
            num2 = float(num2_entry)
            
            if operation == '+':
                calc.add(num2)
            elif operation == '-':
                calc.subtract(num2)
            elif operation == '*':
                calc.multiply(num2)
            elif operation == '/':
                calc.divide(num2)
            elif operation == '^':
                calc.power(num2)
                    
main()