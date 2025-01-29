# działania z plikami

with open('test.log', 'w') as fh:
    fh.write('Powitanie\n')
    fh.write('Kolejne\n')
    fh.write('Jeszcze jedno\n')

with open('test.log', 'a') as fh:
    fh.write('Powitanie\n')
    fh.write('Kolejne\n')
    fh.write('Jeszcze jedno\n')
    fh.write('Dopisane\n')
    

