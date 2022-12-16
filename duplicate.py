# Duplicate
array=[1,1,2,2,3,3,4,4,5,5]
count=0
for i in array:
    count=count+1
empty=[]
for i in range(count-1,-1,-1):
    if array[i] not in empty:
        empty=[array[i]]+empty
print(empty)