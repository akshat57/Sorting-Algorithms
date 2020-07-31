import time

def exchange(a,b):
	temp = a
	a = b
	b = temp

	return a,b


def selection_sort(array):

	N = len(array)
	for i in range(N-1):
		min = i
		for j in range(i+1, N):
			if array[j] < array[min]:
				min = j	
		if min != i:
			array[i], array[min] = exchange(array[i], array[min])


def bubble_sort(array):
	N = len(array)
	for i in range(N-1):
		for j in range(N - i - 1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = exchange(array[j], array[j+1])




def insertion_sort(array):
	N = len(array)
	for i in range(1,N):
		temp = array[i]
		j = i
		while array[j-1] > temp and j > 0 :
			array[j] = array[j-1]
			j -= 1	
		array[j] = temp

