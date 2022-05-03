import time

#iterative binary search
def iterativebinarysearch(arr, lowervalue, highervalue, searchvalue):
  while lowervalue <= highervalue:
    mid = lowervalue + (highervalue - lowervalue) // 2

#check if search value is present at mid
    if arr[mid] == searchvalue:
      return mid

#If search value is greater, ignore left half
    elif arr[mid] < searchvalue:
      lowervalue = mid + 1
#if search value is smaller,ignore right half
    else:
      highervalue = mid - 1
  #if its not present
  return -1

#declare array
start = time.time()
arr = [30,49,56,67,78,211]
searchvalue = 78

results = iterativebinarysearch(arr, 0, len(arr)-1, searchvalue)

if results != -1:
  print("Element is present at index % d" % results)
  print("Execution time is: {}".format(time.time() - start))
else:
  print("Element is not present in array")
  print("Execution time is: {}".format(time.time() - start))
