from random import randint

try :
    min_number = int(input('Please enter the minimum number: '))
except Exception as e :
    print('The minimum number is invalid - Shutting down')
    exit()
    
try :    
    max_number = int(input('Please enter the maximum number: '))
except Exception as e :
    print('The maximum number is invalid - Shutting down')
    exit()
    
if max_number < min_number:
    print('Invalid number - Shutting down')
    exit()

rnd_number = randint(min_number, max_number)
print(rnd_number)