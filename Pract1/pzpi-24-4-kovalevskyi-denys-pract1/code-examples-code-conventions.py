import math
from datetime import datetime

# В.4
import os
import sys

import requests

from myproject.models import Order


# В.1
def calculate_area(radius: float) -> float:
    """Обчислює площу кола за заданим радіусом."""
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним.")
    
    return math.pi * (radius ** 2)


# В.5
MAX_RETRIES = 5

class DataProcessor:
    def __init__(self, data_queue):
        self._data_queue = data_queue
        
    @property
    def is_full(self) -> bool:
        return len(self._data_queue) >= MAX_RETRIES


# В.2
def f(a,b):
 x=a*b # multiply
 if x>100:return x-10
 else:return x


# В.3
THRESHOLD = 100
DISCOUNT = 10

def get_total(price: int, quantity: int) -> int:
    total = price * quantity
    return total - DISCOUNT if total > THRESHOLD else total


# В.6
class ConnectionHandler:
    def __init__(self):
        self.counter = 0

    def run(self):
        # Погано: дублює те, що й так зрозуміло з коду
        self.counter += 1  # Збільшуємо лічильник на 1

        # Добре: пояснює "ЧОМУ", а не "ЩО"
        # Сервер скидає перше з'єднання після перезавантаження,
        # тому запит надсилається двічі.
        self.send_request("ping")
        self.send_request("ping")

    def send_request(self, payload):
        pass


# В.7
def add_numbers(first: int, second: int) -> int:
    """
    Додає два цілих числа.

    Args:
        first (int): Перший доданок.
        second (int): Другий доданок.

    Returns:
        int: Сума двох чисел.

    Example:
        >>> add_numbers(1, 2)
        3
    """
    return first + second


# В.8
"""
[flake8]
max-line-length = 79
extend-ignore = E203
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
"""


# В.9
def test_add_empty_string_returns_zero():
    # Arrange
    calculator = StringCalculator()
    
    # Act
    actual = calculator.add("")
    
    # Assert
    assert actual == 0


# В.10
"""
# Автоматично відформатувати весь код у проєкті
black .

# Перевірити код на дотримання стилю без внесення змін
flake8 .
"""


# В.11
class DateTimeProvider:
    def get_weekday(self) -> int:
        return datetime.now().weekday()

def get_discounted_price(price: int, provider: DateTimeProvider) -> int:
    # 1 - це вівторок у методі weekday()
    if provider.get_weekday() == 1:
        return price // 2
    return price


# В.12
"""
repos:
-   repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
    -   id: black
-   repo: https://github.com/PyCQA/flake8
    rev: 4.0.1
    hooks:
    -   id: flake8
"""


# В.13
import pytest

class StringCalculator:
    def add(self, string_numbers: str) -> int:
        if not string_numbers:
            return 0
        return sum(int(x) for x in string_numbers.split(","))

@pytest.mark.parametrize("inputs, expected", [
    ("0,0,0", 0),
    ("0,1,2", 3),
    ("1,2,3", 6),
])
def test_add_multiple_numbers_returns_sum(inputs, expected):
    calculator = StringCalculator()
    assert calculator.add(inputs) == expected
