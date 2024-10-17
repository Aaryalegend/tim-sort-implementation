def insertion_sort(arr, left, right):
	"""
	A helper function that sorts the array using insertion sort.
    
	Parameters:
    	arr (list): The array to be sorted.
    	left (int): The starting index of the array segment to be sorted.
    	right (int): The ending index of the array segment to be sorted.
	"""
	for i in range(left + 1, right + 1):
    	key_item = arr[i]
    	j = i - 1
    	# Move elements of arr[left..i-1], that are greater than key_item,
    	# to one position ahead of their current position.
    	while j >= left and arr[j] > key_item:
        	arr[j + 1] = arr[j]
        	j -= 1
    	arr[j + 1] = key_item


def merge(arr, left, mid, right):
	"""
	A helper function that merges two sorted sub-arrays into a single sorted array.
    
	Parameters:
    	arr (list): The array containing the sub-arrays.
    	left (int): The starting index of the left sub-array.
    	mid (int): The ending index of the left sub-array / middle index.
    	right (int): The ending index of the right sub-array.
	"""
	# Sizes of the two sub-arrays
	left_size = mid - left + 1
	right_size = right - mid

	# Create temporary arrays
	left_arr = [0] * left_size
	right_arr = [0] * right_size

	# Copy data to temporary arrays
	for i in range(0, left_size):
    	left_arr[i] = arr[left + i]
	for j in range(0, right_size):
    	right_arr[j] = arr[mid + 1 + j]

	# Merge the temporary arrays back into arr[left..right]
	i = 0  # Initial index of first sub-array
	j = 0  # Initial index of second sub-array
	k = left  # Initial index of merged sub-array

	while i < left_size and j < right_size:
    	if left_arr[i] <= right_arr[j]:
        	arr[k] = left_arr[i]
        	i += 1
    	else:
        	arr[k] = right_arr[j]
        	j += 1
    	k += 1

	# Copy the remaining elements of left_arr, if any
	while i < left_size:
    	arr[k] = left_arr[i]
    	i += 1
    	k += 1

	# Copy the remaining elements of right_arr, if any
	while j < right_size:
    	arr[k] = right_arr[j]
    	j += 1
    	k += 1


def tim_sort(arr):
	"""
	The main function that implements TimSort algorithm.
    
	Parameters:
    	arr (list): The array to be sorted.
	"""
	# Minimum run size
	min_run = 32
	n = len(arr)

	# Sort individual sub-arrays of size RUN
	for start in range(0, n, min_run):
    	end = min(start + min_run - 1, n - 1)
    	insertion_sort(arr, start, end)

	# Start merging from size RUN (or 32). It will merge to form size 64, then 128, etc.
	size = min_run
	while size < n:
    	# Pick starting point of the left sub-array
    	for left in range(0, n, size * 2):
        	# Find ending point of the right sub-array
        	mid = min(n - 1, left + size - 1)
        	right = min((left + 2 * size - 1), (n - 1))

        	# Merge the sub-arrays
        	if mid < right:
            	merge(arr, left, mid, right)
    	size *= 2


# Take input from user
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print("Original array:", arr)

# Perform TimSort
tim_sort(arr)

# Output the sorted array
print("Sorted array:", arr)
