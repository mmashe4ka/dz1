class RealNumber:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return RealNumber(self.value + other.value)

    def __str__(self):
        return str(self.value)


class ImaginaryNumber:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return ImaginaryNumber(self.value + other.value)

    def __str__(self):
        return str(self.value) + "i"


class ComplexNumber(RealNumber, ImaginaryNumber):
    def __init__(self, real, imag):
        RealNumber.__init__(self, real)
        ImaginaryNumber.__init__(self, imag)

    def add(self, other):
        real_part = super().add(other).value
        imag_part = super().add(other).value
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return str(self.value) + " + " + str(self.value) + "i"



# Створити два комплексних числа
c1 = ComplexNumber(5, 6)
c2 = ComplexNumber(3, 4)

# Додати два комплексні числа
c3 = c1.add(c2)

# Вивести результат
print(c1, "+", c2, "=", c3)
