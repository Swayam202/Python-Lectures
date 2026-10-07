#Print sum of first 10 even numbers 
sum=0
for i in range(1,20):
    if i%2==0:
        sum+=i
    else:
        sum+=0
        
print(sum)