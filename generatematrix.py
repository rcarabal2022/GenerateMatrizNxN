import random


print('Este programa genera una matriz NxN')
#init variable
nmatrix = 0 #Is the N value
enter = True # while cicle control
matrix=[]
row=[]
col=[]

def genereNxN(n):#genere matrx NxN function
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0, 9))#add aleatory numbers
    
def printmatrix(n):#show matrix in screen
    print("Los valores de la matriz son:")
    for i in matrix:
        print(i)
    

def addrowmatrix(matrix,row):#add col of matrix and create row[]list
    addrow = 0
    j = 0
    for i in matrix:
       addrow = sum(i)
       row.append([])
       row[j].append(addrow)
       j = j +1
    return row
   
    
       
def addcolwmatrix(matrix,col):#add col of matrix and create col[]list
    addcol = 0
    j = 0
    for i in zip(*matrix):
       addcol = sum(i)
       col.append([])
       col[j].append(addcol)
       j = j +1
    return col

def printrow_col(row,col):#show matrix in screen
    print("La suma de las filas son:")
    for i in row:
        print(i)
    print("La suma de las columnas son:")
    for i in col:
        print(i)
    
           
#control enter N value method

while enter:
    #except index error for validate int value
    try:
        nmatrix = int(input('Ingrese el valor de N: '))
    except ValueError:
        print("Debes escribir un número.")
        continue
  
    if nmatrix == 0:
        print ('N debe ser diferente de cero')
    else:
        enter = False

genereNxN(nmatrix)#call function "Generate matrix NxN"
printmatrix(matrix)#call function "Print matrix NxN"
addrowmatrix(matrix,row)#call function "add row matrix NxN"
addcolwmatrix(matrix,col)#call function "add col matrix NxN"
printrow_col(row,col)#call function "print row and col"

    