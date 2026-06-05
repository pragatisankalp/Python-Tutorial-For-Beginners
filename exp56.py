import random
import string
#print(random.random())
# randint() randrange()
# print(random.randint(10,20))
# print(random.randrange(10,20,2))
l=[11,23,34,56,67]
s="catchthecode"
# print(random.choice(l))
# print(random.sample(l,k=3))
# print(random.sample(s,k=5))
letters=string.ascii_letters+string.digits+string.punctuation
# for x in range(8):
#     result=random.choice(letters)
#     print(result,end="")
result=''.join(random.choice(letters)for x in range(8))
print(result)