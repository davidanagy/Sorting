# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
    result = -1 # not found
    # TO-DO: add missing code
    for i, element in enumerate(arr):
        if element == target:
            result = i

    return result


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
      return -1 # array empty

    else:
        # set variable 'found' for the while loop
        found = False
        low = 0
        high = len(arr)-1


        # TO-DO: add missing code
        # define function to save space later
        def find_mid(low, high):
            if (low+high) % 2 == 0:
                # If even, just find the mean.
                # Using floor division so the result is an integer.
                mid = (low+high) // 2
            else:
                # If odd, round the mean up so it's a whole number.
                # (This is arbitrary; could also round down.)
                mid = ((low+high) // 2) + 1
            return mid


        mid = find_mid(low, high)
        
        while found is False:
            # print statement below is for debugging
            #print(low, high, mid)
            if arr[mid] == target:
                # found result
                result = mid
                found = True
            elif low == high:
                # The way this code is written, low==high only happens when
                # we're down to one result, i.e., low == mid == high.
                # In this case, if the above "if" statement isn't True,
                # that means the target isn't in the array.
                result = -1
                found = True
            elif target < arr[mid]:
                # If the target is smaller than the middle array element
                if mid != high:
                    # Most of the time, mid does not equal high.
                    # So we set high equal to mid, then find a new mid.
                    high = mid
                    mid = find_mid(low, high)
                else:
                    # If mid==high, then the above code leads to an infinite loop,
                    # because mid will just continue to equal high always.
                    # Now, this actually only happens when there's only two results left.
                    # That means we can just set low equal to high, which will make
                    # mid equal to low. That way we can run one final check to see if we
                    # find the target, and if we don't, the "low==high" condition above
                    # will end the loop.
                    high = low
                    mid = find_mid(low, high)
            else:
                # If the target is larger than the middle array element
                if mid != low:
                    low = mid
                    mid = find_mid(low, high)
                else:
                    # This follows similar logic to the above, though note that
                    # mid only equals low when the final two elemetns are the leftmost
                    # two in the array, i.e., when low==0 and high==1.
                    low = high
                    mid = find_mid(low, high)

        return result


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    middle = (low+high)//2

    # This was for error-checking
    # print(low, middle, high)
    # if len(arr) != 0:
    #     print(arr[middle])

    if len(arr) == 0:
        return -1 # array empty
    # TO-DO: add missing if/else statements, recursive calls
    elif arr[middle] == target:
        # Found the search term; return the index number
        return middle
    elif low == high:
        # This is the base case--if low==high, that means we're down to a
        # single value. Since we already ran through the above "elif",
        # we know that the value is not equal to the target.
        # That means the target is not in the array, so we return -1.
        return -1
    elif target < arr[middle]:
        # Run through the function again, this time only on the values to
        # the left of middle. This works because we know arr is sorted.
        result = binary_search_recursive(arr, target, low, middle-1)
        return result
    else:
        # Same as above, but for everything to the right of middle.
        result = binary_search_recursive(arr, target, middle+1, high)
        return result
