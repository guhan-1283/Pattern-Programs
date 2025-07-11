n = int(input("Enter Number of rows: ")) # getting number of users
for i in range(1,n+1): # Looping for each row
    for j in range(1,i+1): # loop for printing patterns
        print('*',end=" ")
    print()
