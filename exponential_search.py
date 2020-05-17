
def binarySearch( arr, l, r, x): 
    if r >= l: 
        mid = l + ( r-l ) / 2
          
        if arr[mid] == x: 
            return mid 
          
        if arr[mid] > x: 
            return binarySearch(arr, l,  
                                mid - 1, x) 
          
        # Else he element can only be 

        return binarySearch(arr, mid + 1, r, x) 
          
    # We reach here if the element is not present 
    return -1
  
# Returns the position of first 
# occurrence of x in array 
def exponentialSearch(arr, n, x): 
    # IF x is present at first  
    # location itself 
    if arr[0] == x: 
        return 0
          
    # Find range for binary search  
    # j by repeated doubling 
    i = 1
    while i < n and arr[i] <= x: 
        i = i * 2
      
    # Call binary search for the found range 
    return binarySearch( arr, i / 2,  
                         min(i, n), x) 
      
  
# Driver Code 
arr = [2, 3, 4, 10, 40] 
n = len(arr) 
x = 10
result = exponentialSearch(arr, n, x) 
if result == -1: 
    print "Element not found in thye array"
else: 
    print "Element is present at index %d" %(result) 
