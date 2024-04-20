'''rational program'''
class Rational:
    '''Rational class'''
    def __init__(self,numerator,denominator) -> None:
        if denominator==0:
            raise ValueError("Denominator cannot be zero.")
        if denominator<0:
            self.numerator=-numerator
            self.denominator=-denominator
        else:
            self.numerator=numerator
            self.denominator=denominator

    @property
    def mixed_form(self):
        '''different representation'''
        if self.numerator==0:
            return '0'
        if self.numerator//self.denominator==0:
            return str(self)
        return f'{round(self.numerator/self.denominator)} \
{abs(self.numerator)%self.denominator}/{self.denominator}'

    @mixed_form.setter
    def mixed_form(self,value):
        n,d=value.split('/')
        if ' ' in n:
            m,n=n.split(' ')
            self.numerator=-(int(n)+abs(int(m))*int(d)) if int(m)<0 else (int(n)+int(m)*int(d))
            self.denominator=int(d)
        else:
            self.numerator=int(n)
            self.denominator=int(d)

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        '''make numbers smaller if posible'''
        if self.numerator==0:
            return Rational(0,1)
        for i in range(self.numerator%self.denominator+1,0,-1):
            if self.denominator%i==0 and self.numerator%i==0:
                self.numerator=self.numerator//i
                self.denominator=self.denominator//i
                break
        return self

    def __add__(self,other):
        if isinstance(other,Rational):
            n=self.numerator*other.denominator+self.denominator*other.numerator
            d=self.denominator*other.denominator
            return Rational(n,d).reduce()
    def __sub__(self,other):
        if isinstance(other,Rational):
            n=self.numerator*other.denominator-self.denominator*other.numerator
            d=self.denominator*other.denominator
            return Rational(n,d).reduce()
    def __mul__(self, other):
        n=self.numerator*other.numerator
        d=self.denominator*other.denominator
        return Rational(n,d).reduce()
    def __truediv__(self, other):
        n=self.numerator*other.denominator
        d=self.denominator*other.numerator
        return Rational(n,d).reduce()

    def __eq__(self, other) -> bool:
        return self.numerator*other.denominator==other.numerator*self.denominator
    def __ne__(self, other) -> bool:
        return self.numerator*other.denominator!=other.numerator*self.denominator
    def __lt__(self, other):
        return self.numerator*other.denominator<other.numerator*self.denominator
    def __le__(self, other):
        return self<other or self==other
    def __gt__(self, other):
        return self.numerator*other.denominator>other.numerator*self.denominator
    def __ge__(self, other):
        return self>other or self==other
