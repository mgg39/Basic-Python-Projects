print("Welcome into my python based calculator!\n Please note that you should leave a space in between numbers and signs. \n This calculator can add +, rest -, multiply x, divide \ and raise to the power ^. \n")

equation = input ("Please input your equation: \n")

# addition
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y

# multiplication
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    return x / y

#def elevate
def elevate(x, y):
    return x **y 

class Perceptron: 
   def recognize(self, equation):
    #recognize numbers
    res = [int(i) for i in equation.split() if i.isdigit()]  
    num1 = res[0] 
    num2 = res[1]
    #recognize symbol
    valid_symbols= "+^-/x"
    for element in equation:
        if element in valid_symbols:
         symbol = element 
    self.num1 = num1
    self.num2 = num2
    self.symbol = symbol
    #returns
  # return num1,num2,symbol

   def calculate (self):
    num1 = self.num1
    num2 = self.num2num2 = self.num2
    symbol = self.symbol

    for symbol in equation:
#equations
       if symbol == "+":
           print(num1, "+", num2, "=", add(num1, num2))
 
       elif symbol == "-":
           print(num1, "-", num2, "=", subtract(num1, num2))

       elif symbol == "x":
           print(num1, "x", num2, "=", multiply(num1, num2))

       elif symbol == "/":
           print(num1, "/", num2, "=", divide(num1, num2))
       elif symbol == "^":
           print(num1, "^", num2, "=", elevate(num1,num2))
      #else:
         # print("Sorry ths calculation goes beyond my scope!")

perceptron = Perceptron()
perceptron.recognize(equation)
perceptron.calculate()


print("Thank you for using my calculator!")