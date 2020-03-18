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
    # To help understand what's going on, it may be useful to imagine
    # that we're creating two sub-arrays:
    # arrA = arr[start:mid]
    # arrB = arr[mid:end]
    # I will be consulting these two "fake sub-arrays" in
    # the following comments.
    # Keep in mind that, due to the way "merge_sort_in_place" works,
    # we know that both arrA and arrB are already sorted.
    # The result of this function is that arr[start:end] gets sorted.
    if (start == mid) or (mid == end):
        # If start==mid or mid==end, that means one of the above two
        # imaginary sub-arrays is empty. Since the other is already
        # sorted, that means we're done.
        pass
    else:
        # The goal here is to find out what we want arr[start] to be.
        # Since arrA and arrB are already sorted, that means we only
        # have two options: the first element in arrA--arr[start]--
        # or the first element in arrB--arr[mid].
        if arr[start] <= arr[mid]:
            # In this case, arr[start] is smaller. But arr[start]
            # is already arr[start]! So we don't need to change arr itself.
            # Instead, we effectively want to "remove" the first element in arrA
            # before running through this process again. The way to do this is just
            # to do merge_in_place again, but incrementing "start" by 1.
            # In other words, we re-define arrA to be "arr[start+1:mid]",
            # then run merge_in_place again with this new arrA.
            merge_in_place(arr, start+1, mid, end)
        else:
            # When arr[mid] is smaller than arr[start], things get more complicated.
            # The issue is that we need to make arr[start] equal to arr[mid]
            # **without** losing the original arr[start] value. But we can't just
            # flip them, since we **also** need to keep the original ordering
            # in arrA. Basically, we want to move arr[mid] to the left until it
            # reaches arr[start], and shift everything it moves through to the right.
            for i in reversed(range(start, mid)):
                # This runs us through each number from "start" to the one right
                # before "mid", **reversed**--so the first one we do is "mid-1".
                # Now, we want to switch the value in arr[i] with the value
                # immediately to its right, i.e., arr[i+1]. Since we start with
                # "i" equal to "mid-1", the first element we switch it with is
                # arr[mid]. Then we iterate through each index number from "mid-1"
                # to "start". The end result is the goal I specified earlier:
                # arr[start] becomes arr[mid], and the original arr[start] and everything
                # between it and the original arr[mid] gets shifted 1 to the right.
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # The above line is inspired by this Stack Overflow comment:
                # https://stackoverflow.com/a/2493980/12685847
            merge_in_place(arr, start+1, mid+1, end)
            # Now we want to run through this process again. Recall that arr[mid]
            # has become arr[start], and we've effectively shifted the entirety
            # of arrA 1 to the right. That means arrA now begins at "start+1".
            # In addition, arrB has lost its first element, so arrB
            # now begins at "mid+1". That's why we add 1 to start **and** mid
            # when we do recursion here.

    return arr


def merge_sort_in_place(arr, l, r): 
    # TO-DO
    # The basic idea in this function is that we're running merge sort
    # on arr[l:r+1]. 
    if r - l <= 0:
        # When r-l equals 0 (or lower), that means r==l,
        # so we're running merge sort on arr[l:l+1]. This is just a single
        # value, which is already sorted, so we just pass "arr" back.
        pass
    else:
        # We want to divide the array in half. Like "merge_sort" above,
        # this means doing floor division by 2 on the length of the array.
        # Since the array in question, again, is arr[l:r+1], that means
        # we want to do floor division by 2 on "l + r + 1".
        mid = (l + r + 1) // 2
        # The commented-out print statements are for error debugging.
        #print('begin:', arr, l, mid, r)

        # Now, after splitting arr[l:r+1] in half, we want to recurse
        # "merge_sort_in_place" twice, once on each half.
        # These halves are arr[l:mid] and arr[mid:r].
        # Since "merge_sort_in_place" is an inclusive function--again,
        # we're basically sorting arr[l:r+1]--that means we need the first
        # "l" and "r" to be "l" and "mid-1", and the second to be "mid" and "r".
        arr = merge_sort_in_place(arr, l, mid-1)
        #print('merge_sort 1:', arr)
        arr = merge_sort_in_place(arr, mid, r)
        #print('merge_sort 2:', arr)
        
        # Finally, we now run "merge_in_place". The way I've written that
        # function is **exclusive**, i.e., it does **not** include the "end"
        # value. So we need to add 1 to the "end" argument we're giving it.
        arr = merge_in_place(arr, l, mid, r+1)
        #print('merge_in_place:', arr)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# I looked it up on geeks2geeks, but it seems they lied to me; the real
# timsort is wayyyyy more complicated. So I'm not going to try lol.
# def timsort( arr ):
#     num_runs = len(arr) // 32
#     runs = []
#     for i in range(num_runs):
#         runs.append(arr[i:i+32])

#     def insertion_sort(arr):
#         for i in range(1, len(arr)):
#             element = arr[i]
#             for j in reversed(range(0, i)):
#                 if j > i:
#                     bigger_element = arr[j]
#                     arr[j+1] = bigger_element
#                     arr[j] = element
#                 else:
#                     arr[j+1] = element
#                     break
#         return arr

#     for i, run in enumerate(runs):
#         runs[i] = insertion_sort(run)
    



#     return arr
