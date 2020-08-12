# # Function to search an element x in nearly sorted list A
# def searchElement(A, x):

# 	# search space is A[left..right]
# 	(left, right) = (0, len(A) - 1)

# 	# run till search space is exhausted
# 	while left <= right:

# 		# find middle index mid and compare A[mid - 1], A[mid]
# 		# and A[mid + 1] with the key number
# 		mid = (left + right) // 2

# 		# return mid if middle element is equal to key number
# 		if A[mid] == x:
# 			return mid

# 		# return mid-1 if A[mid - 1] is equal to key number
# 		elif mid - 1 >= left and A[mid - 1] == x:
# 			return mid - 1

# 		# return mid+1 if A[mid + 1] is equal to key number
# 		elif mid + 1 <= right and A[mid + 1] == x:
# 			return mid + 1

# 		# if middle element is less than the key number,
# 		# reduce search space to right sublist A[mid+2..right]
# 		elif x > A[mid]:
# 			left = mid + 2

# 		# if middle element is greater than the key number, reduce
# 		# search space to right sublist A[left..mid-2]
# 		else:
# 			right = mid - 2

# 	# invalid input or number present not in the list
# 	return -1

def binary_search(target, nums):
	"""See if target appears in nums"""

	# We think of floor_index and ceiling_index as "walls" around
	# the possible positions of our target, so by -1 below we mean
	# to start our wall "to the left" of the 0th index
	# (we *don't* mean "the last index")
	floor_index = -1
	ceiling_index = len(nums)

	# If there isn't at least 1 index between floor and ceiling,
	# we've run out of guesses and the number must not be present
	while floor_index + 1 < ceiling_index:

			# Find the index ~halfway between the floor and ceiling
			# We use integer division, so we'll never get a "half index"
			distance = ceiling_index - floor_index
			half_distance = distance // 2
			guess_index = floor_index + half_distance

			guess_value = nums[guess_index]

			if guess_value == target:
					return True

			if guess_value > target:
					# Target is to the left, so move ceiling to the left
					ceiling_index = guess_index
			else:
					# Target is to the right, so move floor to the right
					floor_index = guess_index

	return False

if __name__ == '__main__':

	A = [2, 1, 3, 5, 4, 7, 6, 8, 9]
	key = 5

	index = searchElement(A, key)

	if index != -1:
		print("Element", key, "found at index", index)
	else:
		print("Element found not in the list")
