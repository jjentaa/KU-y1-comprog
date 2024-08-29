import math 

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self) -> float:
        return self.numerator/self.denominator
    
    def add(self, n: int):
        return Fraction(self.numerator+(n*self.denominator), self.denominator)
    
    def __add__(self, other):
        self.suan = self.denominator*other.denominator 
        self.sad1 = self.numerator*other.denominator
        self.sad2 = other.numerator*self.denominator
        return Fraction(self.sad1+self.sad2, self.suan)
    
    def multiply(self, n: int):
        return Fraction(self.numerator*n, self.denominator)
    
    def __mul__(self, other):
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
    
    def __str__(self) -> str:
        if(self.numerator/self.denominator):
            gcd_all = math.gcd(self.numerator, self.denominator)
            return f"{int(self.numerator/gcd_all)} / {int(self.denominator/gcd_all)}"
        return "0 / 1"
    