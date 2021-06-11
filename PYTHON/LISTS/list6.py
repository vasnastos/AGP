namelist=['v','a','s','i','l','i','s']
print(''.join(namelist))
from functools import reduce
print(reduce(lambda y,elem:y+elem,namelist,''))
if list:
    print(namelist)
    print('list is not empty')