# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # given 2 sorted arrays,
    # return a new combined array

    merged_arr = []
   
    # TO-DO
    i = 0
    j = 0
    # perform the actions thru both arrays
    while i < len(arrA) and j < len(arrB):
        # compare the two vlues, choose the smaller one
        if arrB[j] >= arrA[i]:
            merged_arr.append(arrA[i])
            i+=1
        # if not true, merge value from second array (because it is smaller)
        else:
            merged_arr.append(arrB[j])
            j+=1
    # Whichever array remains as the last one, 
    # the remaining values will be pushed into the merged array.
   
    return merged_arr  + arrA[i:] + arrB[j:]




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #  if len( arr ) > 1: 
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
    # TO-DO
    # base-case (easiest case)
    if len(arr) <= 1:
        return arr
    

    # divide the arrays
    half = len(arr) // 2
    left = arr[0:half]
    right = arr[half:]

    return merge(merge_sort(left), merge_sort(right))
    # merging sorted arrays
    # return merge(left, right)


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))



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