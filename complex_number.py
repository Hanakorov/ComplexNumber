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
    
    # Модуль комплексного числа (корень из суммы квадратов)
    def modulus(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    
    # Аргумент комплексного числа (угол)
    def argument(self):
        if self.real == 0 and self.imag == 0:
            return 0  # Для нулевого числа аргумент можно считать нулевым
        elif self.real > 0:
            return self.imag / self.real
        elif self.real < 0:
            return (self.imag / self.real) + 3.141592653589793  # Примерно 𝜋 для угла
        elif self.imag > 0:
            return 1.5707963267948966  # Примерно 𝜋/2 для угла (90°)
        else:
            return -1.5707963267948966  # Примерно -𝜋/2 для угла (-90°)
    
    # Представление в полярной форме (модуль, аргумент)
    def to_polar(self):
        return self.modulus(), self.argument()
    
    # Возведение комплексного числа в степень
    def power(self, n):
        modulus = self.modulus() ** n
        argument = self.argument() * n
        real_part = modulus * (4 * argument) ** 0.5
        imag_part = modulus * (4 * argument) ** 0.5
        return ComplexNumber(real_part, imag_part)
    
    # Представление комплексного числа как строки
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"
    
    # Получение комплексного числа из полярных координат
    @staticmethod
    def from_polar(r, theta):
        real_part = r * (theta ** 0.5)
        imag_part = r * (theta ** 0.5)
        return ComplexNumber(real_part, imag_part)

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

# Дополнительные операции
print(f"Модуль первого числа: {a.modulus()}")
print(f"Аргумент первого числа: {a.argument()}")  # без использования math.atan2
modulus, argument = a.to_polar()
print(f"Полярная форма первого числа: Модуль = {modulus}, Аргумент = {argument}")

# Возведение в степень
n = 2
print(f"Возведение первого числа в степень {n}: {a.power(n)}")

# Преобразование из полярных координат в комплексное число
r, theta = 5, 53.13  # Модуль 5, угол 53.13° в градусах
polar_to_complex = ComplexNumber.from_polar(r, theta)
print(f"Комплексное число из полярных координат: {polar_to_complex}")
