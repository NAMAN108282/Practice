def search_triplets(arr):
  arr.sort()
  triplets = []

  for i in range(len(arr)-2):
    if i>0 and arr[i] == arr[i-1]:
      continue
    left = i+1
    right = len(arr)-1

    while left<right:
      curSum = arr[i] + arr[left] + arr[right]
      if curSum == 0:
        triplets.append([arr[i], arr[left], arr[right]])
        left+=1
        right-=1
        while left<right and arr[left] == arr[left-1]:
          left+=1
        while left<right and arr[right] == arr[right+1]:
          right-=1
      elif curSum<0:
        left+=1
      elif curSum>0:
        right-=1 

  return triplets
