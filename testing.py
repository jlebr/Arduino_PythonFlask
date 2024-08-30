
from functions.logici import switch
from functions.logic import switchAll2DB

def test():
    last_value, fan = switch('Vel 1')
    print(f'Fan: {fan}, Last Value: {last_value}')

def test2():
    last_value, fan = switchAll2DB('Vel 3')
    print(f'Fan: {fan}, Last Value: {last_value}')

if __name__ == '__main__':
    test2()