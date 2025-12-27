p = int(input("enter the number of rows: "))
q = int(input("enter the number of columns: "))
matrix =[[int(input())for i in range(q)]for j in range(p)]
for i in range(p):
    for j in range(q):
        print(format(matrix[i][j],"<4",end =""))
        print()  
