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
    arrA = arr[start:mid]
    arrB = arr[mid:end]
    for i in range(end-start):
        if len(arrA) == 0:
            lowest_B = arrB[0]
            arr[start+i] = lowest_B
            arrB.remove(lowest_B)
        elif len(arrB) == 0:
            lowest_A = arrA[0]
            arr[start+i] = lowest_A
            arrA.remove(lowest_A)
        else:
            lowest_A = arrA[0]
            lowest_B = arrB[0]
            if lowest_A <= lowest_B:
                arr[start+i] = lowest_A
                arrA.remove(lowest_A)
            else:
                arr[start+i] = lowest_B
                arrB.remove(lowest_B)

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if r - l <= 0:
        pass
    else:
        mid = (l + r + 1) // 2
        #print('begin:', arr, l, mid, r)
        if r - l == 1:
            arr = merge_in_place(arr, l, mid, r+1)
            #print('merge in place:', arr)
        else:
            arr = merge_sort_in_place(arr, l, mid-1)
            #print('merge_sort 1:', arr)
            arr = merge_sort_in_place(arr, mid, r)
            #print('merge_sort 2:', arr)
            arr = merge_in_place(arr, l, mid, r+1)
            #print('merge_in_place:', arr)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):
#     num_runs = len(arr) // 32
#     runs = []
#     for i in range(num_runs):
#         runs.append(arr[i:i+32])

#     def insertion_sort(arr):
#         first_element = arr[0]
#         for i in range(1, len(arr)):
#             element = arr[i]
#             for j in reversed(range(0, i)):
#                 if j > i:
#                     bigger_element = arr[j]
#                     arr[j+1] = bigger_element
#                 else:
#                     arr[j+1] = element
#                     break

#     return arr
