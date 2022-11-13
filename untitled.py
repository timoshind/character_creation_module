from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу '
                'для вычисления квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Выводит результат на экран, если ввод положительный"""
    if your_number <= 0:
        return
    result_num: float = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {result_num}')


print(message)
calc(25.5)
