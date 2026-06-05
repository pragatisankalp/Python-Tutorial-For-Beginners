# nums=[2,5,11,15] target=7
#dict_1={}
#7-2=5
#{2:0}
#7-5=2
#[1,0]
def two_sum(nums,target): 
    dict_1={}     
    for x in range(len(nums)): 
        y=target-nums[x] 
        if y in dict_1:
            return [x,dict_1[y]]
        else:
            dict_1[nums[x]]=x
print(two_sum([2,5,11,15],7))