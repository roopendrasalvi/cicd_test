from typing import Union

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
