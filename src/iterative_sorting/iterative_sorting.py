# TO-DO: Complete the selection_sort() function below  O(n^2)
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
#   set the first unsorted element as the minimum
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
#   for each of the unsorted elements
        # LOOP thru remaining array to right!
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                # set element as new minimum
                smallest_index = j 
                # swap
        # if cur_index != smallest_index:
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
     
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):   
    # iterate through the array for the length
    # iterate through the array for the next item minus any sorted items
    # compare the first pair of elements
    # if the RHS is less thean the LHS, swap
    # else, do nothing
    
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr     



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
