def connect(**opcje):
    print(opcje)

connect() # {} - słownik para klucz wartość
connect(a=10) # {'a'}
connect(a=10, name='Radek')

def all_args(*args, **kwargs):
    print(args, kwargs)

all_args()
all_args(1,2,3,4,5,6,7)
all_args(a=10, b=34,name='Radek')
all_args(1, 2, 3, a=10, b=67)