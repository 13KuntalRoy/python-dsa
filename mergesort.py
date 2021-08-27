def merge(list1,list2):

    result=[]

    i,j=0,0
    while i < len(list1) and j < len(list2):
        if list1[i]<list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    result+=list1[i:]
    result+=list2[j:]
    return result

def mergesort(list):
    if(len(list)<=1):
        return list
    mid=int(len(list)/2)
    left = mergesort(list[:mid])
    # print(left)
    right = mergesort(list[mid:])
    # print(right)
    return merge(left,right)


arr=[6,7,4,2,9,1,34,67,32,78,54,23,16,12]
print(mergesort(arr))