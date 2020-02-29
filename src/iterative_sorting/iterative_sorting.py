# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
#     for i in range(0, len(arr) - 1):
# #   set the first unsorted element as the minimum
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
# #   for each of the unsorted elements
#         # LOOP thru remaining array to right!
#         for cur_index in range(i + 1, len(arr)):
#             if arr[cur_index] < arr[smallest_index]:
#                 # set element as new minimum
#                 smallest_index = cur_index 
#                 # swap
#                 arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
#             ++i
    temp = 0

    for i in range(0, len(arr) - 1):
        cur_index = i

        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if cur_index != smallest_index:
            temp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = temp
    return arr

#     repeat (numOfElements - 1) times

#   set the first unsorted element as the minimum

#   for each of the unsorted elements

#     if element < currentMinimum

#       set element as new minimum

#   swap minimum with first unsorted position


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):    
    
    #double loops so that the program can go through each iteration of the array n(the length of the array) times
    #if there are 4 items in an array, the program will iterate through the array a total of 16 times
    #outer loop will execute the inner loop 4 times
    for i in range(0, len(arr) - 1):  
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]: #if item at j is 5 and item at j+1 is 3
                temp = arr[j] #put 5(larger num) in temp
                arr[j] = arr[j + 1] #place the smaller value at j+1 (3) where j was
                arr[j+1] = temp #then put 5(larger value) that was in temp in position j+1
    
    return arr     


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
