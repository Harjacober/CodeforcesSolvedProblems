from fractions import Fraction as frac
n = frac((7 - max(map(int, input().split()))) / 6).limit_denominator(6) 
print("{}/{}".format(n.numerator, n.denominator))
