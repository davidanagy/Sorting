# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(len(merged_arr)):
        # Since each array is sorted, we know that the first element in each
        # is lower than all the rest. So compare each array's first element,
        # and the lowest of the two must be the lowest overall. Then, remove
        # that element and repeat this process.
        # If one array runs out (its length reaches 0), then just ignore it
        # and go through the other array from lowest to highest.
        if len(arrA) == 0:
            lowest_B = arrB[0]
            merged_arr[i] = lowest_B
            arrB.remove(lowest_B)
        elif len(arrB) == 0:
            lowest_A = arrA[0]
            merged_arr[i] = lowest_A
            arrA.remove(lowest_A)
        else:
            lowest_A = arrA[0]
            lowest_B = arrB[0]
            if lowest_A <= lowest_B:
                merged_arr[i] = lowest_A
                arrA.remove(lowest_A)
            else:
                merged_arr[i] = lowest_B
                arrB.remove(lowest_B)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print statements were for error checking
    #print('array:', arr)
    length = len(arr)
    if length in [0,1]:
        # Base case; an array of length 1 is already sorted, so just return it.
        # (Need to include case where array is length 0 in case user tries to input
        # an empty array.)
        pass
    else:
        # Divide array into two halves
        mid = length // 2
        first_half = arr[0:mid]
        second_half = arr[mid:length]
        #print('first half:', first_half)
        #print('second half:', second_half)

        # Sort each half using recursion
        first_half_sorted = merge_sort(first_half)
        second_half_sorted = merge_sort(second_half)
        #print('first half sorted:', first_half_sorted)
        #print('second half sorted:', second_half_sorted)

        # Merge the sorted halves together into a single sorted array
        arr = merge(first_half_sorted, second_half_sorted)
        #print('merged array:', arr)

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
