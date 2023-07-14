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
        print(nmatrix)

#create aleatory number (row and col)
row = []
column = []

for i in range(nmatrix):  
    row[i] = random.randint(0, 9)
    column[i] = random.randint(0, 9)


if nmatrix == 0:
     print('N debe ser diferente de cero(0)')


    