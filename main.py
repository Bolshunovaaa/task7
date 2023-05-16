# Multiparadigmatic  programming languages:Task_7
# Bolshunova Kateryna:IKM-221a

print('Multiparadigmatic  programming languages:Task_7\nKateryna Bolshunova:IKM-221a')
class Complex:
    def __init__(self, r, phi):
        self.r = r
        self.phi = phi

    def __str__(self):
        return '{} * exp(j{})'.format(self.r, self.phi)

    def __add__(self, other):
        new_r = self.r + other.r
        new_phi = self.phi + other.phi
        return Complex(new_r, new_phi)

    def __sub__(self, other):
        new_r = self.r - other.r
        new_phi = self.phi - other.phi
        return Complex(new_r, new_phi)

    def __mul__(self, other):
        new_r = self.r * other.r
        new_phi = self.phi + other.phi
        return Complex(new_r, new_phi)

    def __truediv__(self, other):
        new_r = self.r / other.r
        new_phi = self.phi - other.phi
        return Complex(new_r, new_phi)

    def modulus(self):
        return self.r

z1 = Complex(5, 1) # комплексне число 5 * exp(j1)
z2 = Complex(3, 2) # комплексне число 3 * exp(j2)

print(z1 + z2) # додавання чисел: 8 * exp(j3)
print(z1 - z2) # віднімання чисел: 2 * exp(j-1)
print(z1 * z2) # множення чисел: 15 * exp(j3)
print(z1 / z2) # ділення чисел: 5/3 * exp(j-1)

print(z1.modulus()) # модуль числа: 5


