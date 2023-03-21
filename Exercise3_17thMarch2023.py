def main():
    a = 10
    b = 5
    c = 3
    d = 5
    e = Multiply(a,b)
    print(e)
    f = Exponential(e,c)
    print(f)
    Modulus(f,d)
def Multiply(a,b):
    return(a*b)
def Exponential(e,c):
    return(e**c)
def Modulus(f,d):
    print(f%d)
main()
