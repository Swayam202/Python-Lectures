#Accept two values S and N. Print square of first N number starting from S
s = int(input("Enter S: "))
n = int(input("Enter N: "))

for i in range(s, s+n):
    print(i+i)