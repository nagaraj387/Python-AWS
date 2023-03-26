def main():
    a = 10
    b = 5
    c = 2
    d = Addition(a,b)
    print(d)
    e = Modulus(d,c)
    print(e)
    print(e>a and e == 1)
def Addition(a,b):
    return(a+b)
def Modulus(d,c):
    return(d%c)
main()
