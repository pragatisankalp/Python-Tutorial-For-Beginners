                                                                          # Task 10
"""
In this exercies print 1 to 150 numbers (Both inclusive) but
  1. Insted  of printing multiples of 3,print "Fizz"
  2. Insted  of printing multiples of 5,print "Buzz"
  3. Insted  of printing multiples of both 3 and 5,print "FizzBuzz"
"""
'''
for num in range(1,151):
    if num%5==0 and num%3==0:
        print(f"{num}.FizzBuzz")
    elif num%5==0:
        print(f"{num}.Buzz")
    elif num%3==0:
        print(f"{num}.Fizz")
    else:
        print(num)'''
 
#Discuss the basic data types used in Python. What will be the output of the following Python code?
'''ct = "galgotias"
k = "g"
while k in ct:
  print("1")
  print(k, end=" ")'''
#Interpret the output of the following Python code snippet?
ct = [0, 1, 2, 3] 
x = -2
#Write a python function to print the output, until the termination of the loop occurred.
'''for x not in ct:
    print(x)
    x += 1'''
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")