from enum import Enum

try:
    source = Enum('source', {'username':'admin', 'password':'123455'})
    Number = Enum('Number', ('one', 'two'))
    
except Exception as a:
    print('Error : {}'.format(a))