"""
Given an integer, n, perform the following conditional actions:
If  n is odd, print Not Win
If n is even and in the inclusive range of 2 to 5 , print Win
If  n is even and in the inclusive range of 6 to 20 , print Not Win
If n is even and greater than 20 , print Win

"""
n= int(input('Enter your no: '))
if n%2==1:
    print('Not win')
elif n%2==0 and (n>=2 and n<6):
    print('Win')
elif n%2==0 and(n>=6 and n<21):
    print('Not win')
else:
    print('Win')



"""
  Pooja would like to withdraw X rs from an atm.The cash machine will only transaction:
  
  1. If X is multiple of 5 and withdrawal amount is less than available amount then it displays 
       "Transaction is successfull" otherwise it displays "Transaction is failed."
  2. If withdrawal amount is greater than available amount then it displays" Balace is low."
  3. For successfull withdrawal the bank charges 100 rs.

  Calculate Pooja's account balace after an attempted transaction.
  """
  
Pooja = int(input("Enter the amount you want to withdraw: "))
amt = 551
if (Pooja%5==0):
    print("Transaction Successfull")
    amt = amt - Pooja
    print("Bank Charges exta 100rs for every succesfull Transasction")
    amt = amt - 100 
    
elif(Pooja%5!=0):
    print("Transcation Failed")

if (Pooja>amt):
    print("Balance is low")

