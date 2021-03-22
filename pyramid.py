n=int(input("enter the no of rows:"))
k=0
for i in range(1,n+1):
    k=k+1
    for j in range(1,k+1):
        print(i*j,end=" ")
    print()

