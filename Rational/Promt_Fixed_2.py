class Rational:
    def __init__(self, numerator, denominator) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            self.numerator = -numerator
            self.denominator = -denominator
        else:
            self.numerator = numerator
            self.denominator = denominator
        # self.reduce()

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        if self.numerator == 0:
            self.denominator = 1
            return self
        common = Rational.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        return self

    @property
    def mixed_form(self):
        if self.numerator==0:
            return '0'
        m = '' if self.numerator // self.denominator == 0 else f'{round(self.numerator / self.denominator)} '
        return f'{m}{Rational(abs(self.numerator) % self.denominator, self.denominator)}'

    @mixed_form.setter
    def mixed_form(self, value):
        n, d = value.split('/')
        if ' ' in n:
            m, n = n.split(' ')
            self.numerator = -(int(n) + abs(int(m)) * int(d)) if int(m) < 0 else (int(n) + int(m) * int(d))
            self.denominator = int(d)
        else:
            self.numerator = int(n)
            self.denominator = int(d)
        # self.reduce()

    # @property
    # def mixed_form(self):
    #     return self.mixed_form

    # @mixed_form.setter
    # def mixed_form(self, value):
    #     return self.mixed_form_setter(value)

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

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
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Rational(n, d).reduce()

    def __truediv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Rational(n, d).reduce()

    def __eq__(self, other) -> bool:
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other) -> bool:
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator \
               or self.numerator * other.denominator == other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator \
               or self.numerator * other.denominator == other.numerator * self.denominator
