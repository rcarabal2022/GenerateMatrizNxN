import random

print('Este programa genera una matriz NxN')
#init nmatriz
nmatrix = 0
#   excepctions manager
#check numeric value 
def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
 #check if numeric is integer  
def isinstance(s):
    try:
        int(s)
        return True
    except ValueError:
        return False    
   
#enter N value method
def enterN():
        nmatrix = input('ingrese el valor de N: ')


#voy por aqui.....
        if nmatrix is not int:
            print('N debe ser un número entero')
        else:
            if nmatrix == 0:
                print('N debe ser diferente de cero(0)')


    