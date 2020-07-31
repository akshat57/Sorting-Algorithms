def merge(array, reverse_array, left, right, m):
	#Copying to reverse_array
	for i in range(left, m+1):
		reverse_array[i] = array[i]

	for i in range(m+1, right+1):
		reverse_array[i] = array[right + m + 1 - i]

	i = left
	j = right
	for k in range(left, right + 1):
		if reverse_array[i] < reverse_array[j]:
			array[k] = reverse_array[i]
			i += 1
		else:
			array[k] = reverse_array[j]
			j -= 1


def merge_sort(array, reverse_array, left, right):
	if right - left > 0:
		m = (left + right)//2
		merge_sort(array, reverse_array, left, m)
		merge_sort(array, reverse_array, m+1, right)
		merge(array, reverse_array, left, right, m)

