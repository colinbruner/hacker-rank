import math

# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        if isinstance(no, __class__):
            self.real = self.real + no.real
            self.imaginary = self.imaginary + no.imaginary
        else:
            raise (ValueError("Not supported."))

    def __sub__(self, no):
        if isinstance(no, __class__):
            self.real = self.real - no.real
            self.imaginary = self.imaginary - no.imaginary
        else:
            raise (ValueError("Not supported."))

    def __mul__(self, no):
        pass

    def __truediv__(self, no):
        pass

    def mod(self):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == "__main__":
    a, b = map(int, input().split())
    x, z = map(int, input().split())

    c = Complex(a, b)
    d = Complex(x, z)
    c + d
    print(c)
    c - d
    print(c)
