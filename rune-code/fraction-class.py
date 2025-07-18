def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        if not (isinstance(top, int) and isinstance(bottom, int)):
            raise TypeError("Numerator and Denominator have to be integers.")
        cmmn = gcd(top, bottom)
        self.num = top // cmmn
        self.den = bottom // cmmn

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num

    def __lt__(self, other_fraction):
        if self.den == other_fraction.den:
            return self.num < other_fraction.num
        else:
            return self.num * other_fraction.den < self.den * other_fraction.num
        
    def __le__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num <= second_num

    def __gt__(self, other_fraction):
        if self.den == other_fraction.den:
            return self.num > other_fraction.num
        else:
            return self.num * other_fraction.den > self.den * other_fraction.num

    def __ge__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num >= second_num
    
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num , new_den)
    
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        if other_fraction.num == 0:
            return "Cannot divide by zero"
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num , new_den) 
    
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
print(x + y)
print(x == y)
print(x - y)
print(x * y)
print(x / y)