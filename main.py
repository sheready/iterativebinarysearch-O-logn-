import time

#iterative binary search
def iterativebinarysearch(arr, lowervalue, highervalue, searchvalue):
  while lowervalue <= highervalue:
    mid = lowervalue + (highervalue - lowervalue) // 2

#check if x is present at mid
    if arr[mid] == searchvalue:
      return mid

#If x is greater, ignore left half
    elif arr[mid] < searchvalue:
      lowervalue = mid + 1
#if x is smaller,ignore right half
    else:
      highervalue = mid - 1
  #if its not present
    return -1

#declare array
start = time.time()
arr = [56,90,78,49,211,67,30]
searchvalue = 78

results = iterativebinarysearch(arr, 0, len(arr)-1, searchvalue)

if results != -1:
  print("Element is present at index % d" % results)
  print("Execution time is: {}".format(time.time() - start))
else:
  print("Element is not present in array")
  print("Execution time is: {}".format(time.time() - start))
