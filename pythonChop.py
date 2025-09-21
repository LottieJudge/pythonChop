def binaryChop(array, target):
  left = 0 
  right = len(array) - 1

  while left <= right: 
    mid = (left + right) // 2 
    
    if array[mid] == target:
      return mid 
    if array[mid] < target:
      left = mid + 1
    else: 
      right = mid -1 

  return -1 

list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 3

result = binaryChop(list, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")