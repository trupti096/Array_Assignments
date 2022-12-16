a=[4,2,6,5,7,1]
# count=0
# for i in array:
#     count=count+1
# for i in range(1,count):
#     min = array[i]
#     j=j-1
#     while j>=0 and min<array[j]:
#         array[j+1] = array[j]
#         j=j-1
#     array[j+1] = min
# print(array)


for i in range(1,len(a)):
    j=0
    key = a[i]
    j=j-1
    while j>=0 and key<a[j]:
        a[j+1] = a[j]
        j=j-1
    a[j+1] = key
print(a)