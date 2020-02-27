# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
# loop through n-1 elements
# repeat (numOfElements - 1) times
    for i in range(0, len(arr) - 1):
#   set the first unsorted element as the minimum
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
#   for each of the unsorted elements
        while i < len(arr):
            for value in arr[i]:
                if value[i] < value[smallest_index]:
                    # set element as new minimum
                    smallest_index = cur_index
                    # swap
                    value[cur_index], value[smallest_index] = value[smallest_index], value[cur_index]
                ++i
    return arr

#     repeat (numOfElements - 1) times

#   set the first unsorted element as the minimum

#   for each of the unsorted elements

#     if element < currentMinimum

#       set element as new minimum

#   swap minimum with first unsorted position


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr