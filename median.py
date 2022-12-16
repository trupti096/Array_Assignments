# Median
# Without Sort
array=[1,5,7,3,9]
count=0
for i in array:
    count=count+1
    for i in range(count):
        if count % 2==0:
            median1=array[count//2]
            median2=array[count//2-1]
            median=(median1 + median2)/2
        else:
            median=array[count//2]
print(str(median))



# Sort
array=[1,5,7,3,9]
count=0
for i in array:
    count=count+1
    for i in range(count):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
print(array)
if count % 2==0:
    median1=array[count//2]
    median2=array[count//2-1]
    median=(median1 + median2)/2
else:
    median=array[count//2]
print(str(median))
    

