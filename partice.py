def searchindexmethod(list, query):
    low = 0
    high = len(list) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if list[mid] == query:
            found = True
            return mid
        elif list[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    if not found:
        return low

print(searchindexmethod([2,3,4,5,6,7,8,9,10], 1))
