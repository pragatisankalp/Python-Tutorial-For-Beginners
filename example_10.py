import time
x=time.time()
fruits={"apple","bananna"}
fruits_1={"cherry","orange"}
fruits.add("cherry")
#print(fruits)
#fruits.add("cherry")
#print(fruits)
fruits.remove("apple")
print(fruits)
print("Excution time is",time.time()-x)