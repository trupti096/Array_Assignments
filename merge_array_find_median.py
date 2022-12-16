array1=[1,2,3,4,5]
array2=[11,10,9,8,7,6]
array3=array1+array2
print(sum)
count=0
for i in array3:
    count=count+1
    for i in range(count):
        key=array3[i]
        j=i-1
        while j>=0 and key<array3[j]:
            array3[j+1]=array3[j]
            j=j-1
        array3[j+1]=key
print(array3)
if count % 2==0:
    median1=array3[count//2]
    median2=array3[count//2-1]
    median=(median1 + median2)/2
else:
    median=array3[count//2]
print(str(median))