array=[5,4,3,2,1]
count=0
for i in array:
    count=count+1
for i in range(count-1):
    min=i
    for j in range(i+1,count):
        if array[i] > array[j]:
            min=j
        array[i],array[min]=array[min],array[i]
print(array)