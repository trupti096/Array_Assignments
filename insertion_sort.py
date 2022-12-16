array=[7,5,8,3,2]
count=0
for i in array:
    count=count+1
for i in range(1,count):
    min=array[i]
    j=i
    while j!=0 and min<array[j-1]:
        array[j],array[j-1] = array[j-1],array[j]
        j=j-1
print(array)