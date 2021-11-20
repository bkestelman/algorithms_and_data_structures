def binary_search_simple_recursive(arr, e):
    """
        Simple recursive implementation of binary search that does not 
        need to keep track of left and right bounds.
        @param arr list
        @param e element
        @return index of e, or its insertion point if not found
    """
    if len(arr) == 0:
        return 0
    mid = len(arr) // 2 # exact middle for odd len, just right of middle for even len
    if arr[mid] == e:
        return mid
    if arr[mid] > e:
        return binary_search_simple_recursive(arr[:mid], e)
    else:
        return mid+1 + binary_search_simple_recursive(arr[mid+1:], e)

def binary_search_recursive(arr, e, l=0, r=None):
    """
        Recursive implementation of binary search 
        @param arr list
        @param e element
        @param l left bound
        @param r right bound
        @return index of e, or -1 if not found
    """
    if r is None:
        r = len(arr)
    if r <= l:
        return -1
    mid = (l + r) // 2
    if arr[mid] == e:
        return mid
    if arr[mid] > e: 
        return binary_search_recursive(arr, e, l=l, r=mid)
    else:
        return binary_search_recursive(arr, e, l=mid+1, r=r)
    
def binary_search_iterative(arr, e, l=0, r=None):
    """
    """
    if r is None:
        r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == e:
            return mid
        if arr[mid] > e:
            r = mid
        else:
            l = mid + 1
    return -1
