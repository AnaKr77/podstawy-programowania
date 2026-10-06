from cmath import sqrt

if __name__ == '__main__':
    print("Podaj a,b,c")
    a = int(input())
    b = int(input())
    c = int(input())
    delta=pow(b,2)-4*a*c
    print(delta)
    if(delta<0):
        print("Funkcja nie ma miejsc zerowych")
    elif(delta==0):
        x=((-1)*b)/(2*a)
        print("Funkcja ma jedno miejsce zerowe i wynosi: ")
        print(x)
    else:
        x1=((-1)*b-sqrt(delta))/2*a
        x2 = ((-1) * b + sqrt(delta)) / 2 * a
        print("Funkcja ma dwa miejsce zerowe, ktore wynosza: ")
        print(x1)
        print(x2)

