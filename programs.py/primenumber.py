n= int(input("Find sum of prime numbers upto : "))  
sum = 0 
for num in range(2, n + 1):  
    i = 0  
    for i in range(2, num):  
        if (int(num % i) == 0):  
            i = num  
            break
     #If the number is prime then add it.  
    if i is not num:  
        sum += num  
print("\nSum of all prime numbers upto", n, ":", sum)















