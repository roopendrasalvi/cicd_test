from typing import Union
import math

class Calculator:
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))        # Output: 8
    print(calc.subtract(5, 3))   # Output: 2
    print(calc.multiply(5, 3))   # Output: 15
    print(calc.divide(5, 3))     # Output: 1.6666666666666667