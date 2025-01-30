# funkcja wewnętrzna, zagnieżdzona
# dekorator wykorzystuje zasadę funkcji wew

def fun1():
    print('To jest fun1')

    def fun2():
        print('To jest fun2')

    return fun2  # zwraca adres funkcji


fun1()  # To jest fun1
xFun = fun1()
print(type(xFun))  # <class 'function'>
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000021845D74A40>
xFun()  # To jest fun2
xFun()
print('Inne rzeczy')
xFun()
