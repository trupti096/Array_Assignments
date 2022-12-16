# Reverse
array=[1,2,3,4,5]
empty=[]
for i in array:
    empty=[i]+empty
print(empty)