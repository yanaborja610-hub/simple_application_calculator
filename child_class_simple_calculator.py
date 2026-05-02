from parent_class_simple_calculator import CalculatorParentClass

class BasicCalculator(CalculatorParentClass):
    def add_numbers(self, a, b):
        return a + b

    def subtract_numbers(self, a, b):
        return a - b

    def multiply_numbers(self, a, b):
        return a * b

    def divide_numbers(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot be divided by zero"

