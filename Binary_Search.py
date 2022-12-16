array=[1,2,3,4,5,6,7,8,9,10]
def binarySearch(array,start,end,number):
    if start<end:
        mid=start+(end-start)//2
        if array[mid]==number:
            return mid
        elif array[mid] > number:
            return binarySearch(array,start,mid-1,number)
        elif array[mid] < number:
            return binarySearch[array,mid+1,end,number]
        else:
            return "element is not in array"
array=[1,2,3,4,5,6,7,8,9,10]
number=7
print(binarySearch(array,0,len(array)-1,number))


# def binarySearch(array,start,end,number):
#     if start<=end:
#         middle=start+(end-start)//2
#         if array[middle]==number:
#             return middle
#         elif array[middle]>number:
#             return binarySearch(array,start,middle-1,number)
#         elif array[middle]<number:
#             return binarySearch(array,middle+1,end,number)
#     else:
#         return "Element is not there."
# array=[1,2,3,4,5,6,7,8]
# number=7
# print(binarySearch(array,0,number-1,number))