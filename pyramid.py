# for odd number of strings
n = int(input("Enter Number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print('*',end=" ")
    print()

# for even number of strings
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print('* ',end="")
    print()
