class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            self.numerator = -numerator
            self.denominator = -denominator
        else:
            self.numerator = numerator
            self.denominator = denominator

    @property
    def mixed_form(self):
        if self.numerator == 0:
            return '0'
        if abs(self.numerator) < self.denominator:
            return str(self)
        whole_part = round(self.numerator / self.denominator)
        numerator_part = abs(self.numerator) % abs(self.denominator)
        return f'{whole_part} {numerator_part}/{self.denominator}' if numerator_part != 0 else f'{whole_part}'

    @mixed_form.setter
    def mixed_form(self, value):
        n, d = value.split('/')
        if ' ' in n:
            m, n = n.split(' ')
            self.numerator = -(int(n) + abs(int(m)) * int(d)) if int(m) < 0 else (int(n) + int(m) * int(d))
        else:
            self.numerator = int(n)
        self.denominator = int(d)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        if self.numerator == 0:
            return Rational(0, 1)
        gcd = self._gcd(self.numerator, self.denominator)
        return Rational(self.numerator // gcd, self.denominator // gcd)

    def __add__(self, other):
        if isinstance(other, Rational):
            n = self.numerator * other.denominator + self.denominator * other.numerator
            d = self.denominator * other.denominator
            return Rational(n, d).reduce()

    def __sub__(self, other):
        if isinstance(other, Rational):
            n = self.numerator * other.denominator - self.denominator * other.numerator
            d = self.denominator * other.denominator
            return Rational(n, d).reduce()

    def __mul__(self, other):
        if isinstance(other, Rational):
            n = self.numerator * other.numerator
            d = self.denominator * other.denominator
            return Rational(n, d).reduce()

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ValueError('Denominator cannot be zero.')
            n = self.numerator * other.denominator
            d = self.denominator * other.numerator
            return Rational(n, d).reduce()

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self > other or self == other
