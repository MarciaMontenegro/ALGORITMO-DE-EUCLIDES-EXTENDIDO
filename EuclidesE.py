def EuclidesE(a, b):
    # Base Case
    if a == 0 :
        return b,0,1

    mcd,x1,y1 = EuclidesE(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return mcd,x,y


a = int(input("Ingrese el primer número a: "))
while a < 0:
    print("El numero ingresado debe ser positivo")
    a=int(input("Ingrese el primer número a: "))

b = int(input("Ingrese el segundo número b: "))
while b < 0:
    print("El numero ingresado debe ser positivo")
    b=int(input("Ingrese el segundo número b: "))
    
m, x, y = EuclidesE(a, b)
print("Euclides Extendido de(", a , "," , b, ") = ")
print("Mcd: ",m)
print("Valor de x: ",x)
print("Valor de y: ",y)
