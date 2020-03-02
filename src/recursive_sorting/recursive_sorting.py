# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # starting at beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
   
    # TO-DO
    i = 0
    j = 0
    # perform the actions thru both arrays
    while i < len(arrA) and j < len(arrB):
        # if second array's value is larger than first array's value
        # if true, add it to the new merged array and go to next element in the array
        if arrB[j] > arrA[i]:
            merged_arr.append(arrA[i])
            ++i
        # if not true, merge value from second array (because it is smaller)
        else:
            merged_arr.append(arrB[j])
            ++j
    # Whichever array remains as the last one, 
    # the remaining values will be pushed into the merged array.
    while i < len(arrA):
        merged_arr.append(arrA[i])
        ++i

    while j < len(arrB):
        merged_arr.append(arrB[j])
        ++j

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #  if len( arr ) > 1: 
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
    # TO-DO

    return arr


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

def merge_sort( arr ):
    if len( arr ) > 1: 
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces

def merge_helper( a, b ):
    merged_arr = []

    # starting at beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    return merged_arr

