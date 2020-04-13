# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

             
     # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        print('value i', arr[i])
        # # print('index i', i)
        for j in range(0, len(arr)-i-1):
            print('value j', arr[j])
        #     # print('index j', j)
            if arr[j] > arr[j+1]:
                print(arr[j], arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr

arr = [1,5,6,3,4,8]
print(bubble_sort(arr))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr