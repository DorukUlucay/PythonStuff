#base class. optional
class ICalculator:
    def Add():
        return None

#concrete class
class Calculator(ICalculator):
    def Add(self, First, Second):
        return First + Second

#proxy
class CalculatorProxy(ICalculator):
    C = Calculator()
    def Add(self, First, Second):
        #method in base class automatically overriden
        print("Calculating...")
        result = str(First) + " + " + str(Second) + " = " + str(self.C.Add(First, Second))
        return result

#instance of proxy
calc = CalculatorProxy()

print(calc.Add(3,4))
