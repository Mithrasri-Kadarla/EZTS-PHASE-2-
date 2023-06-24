#get one matrix as input and display diagonal elements,non-digonal elements,upper,lower

# A basic code for matrix input from user
 
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
 
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
'''print("Diagonal elements:")
if (i==j):
    print(matrix[i][j])
else:
    print("NON Diagonal Elements")
    print(matrix[i][j])
print("Upper:")
if(i<j):
    print(matrix[i][j])
elif(i>j):
    print(matrix[i][j])'''
