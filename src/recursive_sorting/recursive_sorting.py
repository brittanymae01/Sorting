# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    aIndex = 0
    bIndex = 0
    for i in range(len(merged_arr)):
        if aIndex == len(arrA) and bIndex <= len(arrB):
            merged_arr[i] = arrB[bIndex]            
            bIndex += 1
        elif aIndex <= len(arrA) and bIndex == len(arrB):
            merged_arr[i] = arrA[aIndex]            
            aIndex += 1
        elif arrA[aIndex] < arrB[bIndex]:
            merged_arr[i] = arrA[aIndex]
            aIndex += 1
        elif arrA[aIndex]> arrB[bIndex]:
            merged_arr[i]= arrB[bIndex]
            bIndex += 1

    return merged_arr


a = [1,3,4]
b = [2,5,7]
print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr)// 2])
        right = merge_sort(arr[len(arr)// 2:])
        arr = merge(left, right)

    return arr

hello = [5,3,7,2,8,9,1,3,0]
print(merge_sort(hello))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
