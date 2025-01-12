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
    
    # Аргумент комплексного числа
    def argument(self):
        if self.real == 0 and self.imag == 0:
            return 0  # Для нулевого числа аргумент можно считать нулевым
        elif self.real > 0:
            return self.imag / self.real
        elif self.real < 0:
            return (self.imag / self.real) + 3.141592653589793  # Примерно 𝜋
        elif self.imag > 0:
            return 1.5707963267948966  # Примерно 𝜋/2 для угла (90°)
        else:
            return -1.5707963267948966  # Примерно -𝜋/2 для угла (-90°)
    
    # Конъюгат комплексного числа
    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)
    
    # Сравнение комплексных чисел
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.modulus() < other.modulus()
    
    def __le__(self, other):
        return self.modulus() <= other.modulus()
    
    def __gt__(self, other):
        return self.modulus() > other.modulus()
    
    def __ge__(self, other):
        return self.modulus() >= other.modulus()
    
    # Возведение в степень
    def power(self, n):
        modulus = self.modulus() ** n
        argument = self.argument() * n
        real_part = modulus * (4 * argument) ** 0.5
        imag_part = modulus * (4 * argument) ** 0.5
        return ComplexNumber(real_part, imag_part)
    
    # Извлечение корня
    def sqrt(self):
        modulus = self.modulus() ** 0.5
        argument = self.argument() / 2
        real_part = modulus * (4 * argument) ** 0.5
        imag_part = modulus * (4 * argument) ** 0.5
        return ComplexNumber(real_part, imag_part)
    
    # Представление комплексного числа как строки
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"
    
    # Вывод в полярной форме или стандартной
    def display(self, polar=False):
        if polar:
            r, theta = self.to_polar()
            print(f"Полярная форма: {r}(cos({theta}) + i sin({theta}))")
        else:
            print(f"Комплексное число: {self.real} + {self.imag}i")

# Пример использования
a = ComplexNumber(3, 4)
b = ComplexNumber(1, -2)

print(f"Первое число: {a}")
print(f"Второе число: {b}")

# Операции
print(f"Сложение: {a + b}")
print(f"Вычитание: {a - b}")
print(f"Умножение: {a * b}")
print(f"Деление: {a / b}")

# Дополнительные операции
print(f"Конъюгат первого числа: {a.conjugate()}")
print(f"Модуль первого числа: {a.modulus()}")
print(f"Аргумент первого числа: {a.argument()}")
a.display(polar=True)

# Сравнение комплексных чисел
print(f"Первое число равно второму? {a == b}")
print(f"Первое число больше второго? {a > b}")

# Возведение в степень
n = 2
print(f"Возведение первого числа в степень {n}: {a.power(n)}")

# Извлечение корня
print(f"Корень из первого числа: {a.sqrt()}")
