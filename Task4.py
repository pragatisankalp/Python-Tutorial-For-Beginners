                     #Task 4
"""
Find out common city between UP and NCR.
I have provided two variables:
up_city={"Noida","Kanpur","Lucknow"}
ncr_city=set() 

In this task:
1. Ask the user for the name of city. Add this name to ncr_city set provided.
2. Finally print out a set that contains only the name of city if the city is in the up_city.

you will want to intersection between two sets and print the result out.

"""
up_city={"Noida","Kanpur","Lucknow"}
ncr_city=set() 
city=input("Enter the city name:")
ncr_city.add(city)
print(f"NCR city is {ncr_city}")
print(up_city.intersection(ncr_city))




