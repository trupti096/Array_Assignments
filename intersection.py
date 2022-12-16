# Intersection
array1=[1,2,3,4,5]
array2=[4,5,6,7,8,9,10]
count=0
for i in array1:
    count=count+1
empty=[]
for i in range(count-1,-1,-1):
    if (array1[i] not in empty) and (array1[i] in array2):
        empty=[array1[i]]+empty
print(empty)