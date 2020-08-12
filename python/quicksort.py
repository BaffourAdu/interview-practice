"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):

  pivot = len(array) - 1
  iterator = 0
  
  while iterator < pivot:
    if array[iterator] > array[pivot]:
      previous_index = pivot - 1 
      previous = array[previous_index] 

      if iterator != previous_index:
        array[previous_index] = array[pivot] 
  
        array[pivot] = array[iterator] 

        array[iterator] = previous 
      else:  
        last_value = array[pivot]
        array[pivot] = array[iterator] 
        array[iterator] = last_value

      pivot = pivot - 1 

    if array[iterator] < array[pivot]:
      iterator = iterator + 1


  left_pivot = pivot - 1
  right_pivot =  pivot + 1
  left_iterator = 0
  right_iterator = len(array) - 1

  print(left_pivot, left_iterator, right_iterator, right_pivot)
  while left_pivot < left_iterator
    if left_iterator < array[left_pivot]:
      left_previous = array[left_pivot-1]


  # while right_pivot < right_iterator
  #   if < array[left_pivot] 

  return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))