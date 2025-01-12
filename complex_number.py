class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  # Действительная часть
        self.imag = imag  # Мнимая часть
    
    # Сложение комплексных чисел
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    # Вычитание комплексных чисел
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    # Умножение комплексных чисел
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    # Деление комплексных чисел
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)
    
    # Модуль комплексного числа
    def modulus(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    
    # Строковое представление комплексного числа
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"
    
# Пример использования
a = ComplexNumber(3, 4)  # Комплексное число 3 + 4i
b = ComplexNumber(1, -2)  # Комплексное число 1 - 2i

print(f"Первое число: {a}")
print(f"Второе число: {b}")

# Операции
print(f"Сложение: {a + b}")
print(f"Вычитание: {a - b}")
print(f"Умножение: {a * b}")
print(f"Деление: {a / b}")
print(f"Модуль первого числа: {a.modulus()}")
