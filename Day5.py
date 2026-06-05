# Subarray 
#  Question 1: print subarray of size k=3
"-------------------------------------------------------"
# Bruteforce method
'''a = [-2, 5, 6, -5, 4]
s = len(a)
k = 3
nestedlist=[]
for i in range(0, s - k + 1):
    subarray = []
    for j in range(i, i + k):
        subarray.append(a[j])
    nestedlist.append(subarray)
    #print(subarray)
print(nestedlist)'''

"------------------------------------------------------------------"
# Bruteforce Method
# Question 2. find the max sum of subarray of size k
'''a=[-2,5,6,-5,4]
s=len(a)
k=3
msum=float('-inf')
for i in range(0,s-k+1):
    csum=0
    for j in range(i,i+k):
       csum=csum+a[j]
    if msum<csum:
        msum=csum
print(msum)'''

# Optimized Method----Sliding Window
'''a=[-2,5,6,-5,4]
l=len(a)
i=0
j=0
csum=0
msum=float('-inf')
k=3
wsize=j-i+1
while(j<l):
    csum=csum+a[j]      
    if j-i+1<k:              
        j=j+1

    elif (j-i+1==k):
        msum=max(csum,msum)
        csum=csum-a[i]
        i=i+1
        j=j+1
print(msum)'''
"--------------------------------------------------------------------"
#print the first -ve number in every window of size k
arr=[12,-1,-7,8,-15,13,30,80]