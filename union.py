# Union
array1=[1,2,3,4,5]
array2=[4,5,6,7,8,9,10]
count=0
for i in array1:
    count=count+1                    
empty=[]
for i in range(count+1,-1,-1):
    if array2[i] not in empty:
        empty=[array2[i]]+empty  
for i in range(count-1,-1,-1):
    if array1[i] not in empty:
        empty=[array1[i]]+empty
print(empty)