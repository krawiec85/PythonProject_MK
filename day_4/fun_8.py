def all_params(a, b, c=42, d=256):
    print(f'{a=}, {b=}')
    print(f'{c=}, {d=}')

all_params(1,2)
all_params(1,2, 3, 4)
all_params(1,2, c=3, d=4)
all_params(a=10, b=90)