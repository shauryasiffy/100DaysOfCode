r1 = ["0","0","0"]
r2 = ["0","0","0"]
r3 = ["0","0","0"]
matrix=[r1,r2,r3]
#print(matrix[2][2])
mark=list(input("where do you wanna place the marker?"))
a=int(mark[0])
b=int(mark[1])

row=matrix[b-1]
row[a-1]="X"
print(f"{r1}\n{r2}\n{r3}")
