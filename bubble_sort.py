array=[5,4,2,1,3]
count=0
for i in array:
    count=count+1
for i in range(count-1):
    for j in range(count-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
print(array)