def main():
    a = 5
    addition(a)
    substraction(a)
    multiply(a)
    divison(a)
    modulus(a)
    exponential(a)
def addition(a):
    a += 3 # a equals to a+3
    print(a)
def substraction(a):
    a -= 3
    print(a)
def multiply(a):
    a *= 3
    print(a)
def divison(a):
    a /= 3
    print(a)
def modulus(a):
    a %= 3
    print(a)
def exponential(a):
    a **= 3
    print(a)
main()