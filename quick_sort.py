from basic_sorting_algorithms import exchange

def find_pivot(array, left, right):
	return array[right]


def partition(array, left, right):

	pivot = find_pivot(array, left, right)

	i = left-1 
	j = right

	while i < j:
		i += 1
		while i < right and array[i] <= pivot:
			i +=1
		
		while array[j] >=  pivot and j> left:
			j -= 1
		
		if i < j :
			array[i], array[j] = exchange(array[i], array[j])
	 	
	array[i], array[right] = exchange(array[i], array[right])	
	return i



def quick_sort(array, left, right):
	
	if right > left:
		i = partition(array, left, right)
		quick_sort(array, left, i-1)
		quick_sort(array, i+1, right)


