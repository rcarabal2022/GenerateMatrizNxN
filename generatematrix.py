import random


print('Este programa genera una matriz NxN')
#init variable
nmatrix = 0 #Is the N value
row = []
column = []
addrow = 0
addcol = 0
enter = True # while cicle control
matrix=[]
def genereNxN(n):#genere matrx NxN function
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0, 9))#add aleatory numbers
    
def printmatrix(n):#show matrix in screen
    print("Los valores de la matriz son:")
    for i in matrix:
        print(i)
    

def addrowmatrix(matrix):#add row of matrix
    addrow = 0
    row= []
    for i in matrix:
       addrow = sum(i)
       row.append([])
       print (row)
       
       
# sumaFilas = lambda matriz: [sum(i) for i in matriz]

# sumaColumnas = lambda matriz: [sum(i) for i in zip(*matriz)]

# def addcolmatrix(n):#add col of matrix
#      for i in matrix:
#         addcol = addcol + i 

        
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
addrowmatrix(matrix)#call function "add row matrix NxN"

                    #call function "add col matrix NxN"
                    #call function "printaddmatrix"

    