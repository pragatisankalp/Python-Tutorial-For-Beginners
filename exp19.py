for num in range(2,10):
    for x in range(2,num):
        if num%x==0:
            print(f"{num} is not prime no")
            break
    else:
        print(f"{num} is prime no")
            
