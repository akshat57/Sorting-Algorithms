import pickle	
from generate_test_cases import *
from basic_sorting_algorithms import *
from quick_sort import *
from merge_sort import *

def read_test_case(flag = 'unsorted'):
	if flag == 'unsorted':
		a_file = open("test_case.pkl", "rb")
		output = pickle.load(a_file)
		a_file.close()
	else:
		a_file = open("sorted_test_case.pkl", "rb")
		output = pickle.load(a_file)
		a_file.close()

	return output

def do_python_sort():
	print('Doing python sort :')
	
	array_u = read_test_case('unsorted')
	start = time.time()
	array_u.sort()
	print('Time Unsorted :', time.time() - start)

	array_s = read_test_case('sorted')
	start = time.time()
	array_s.sort()
	print('Time Sorted :', time.time() - start)
	
	print('')

	return array_u, array_s

def do_selection_sort():
	print('Doing selection sort :')        
	
	array_u = read_test_case('unsorted')
	start = time.time()
	selection_sort(array_u)
	print('Time Unsorted :', time.time() - start)

	array_s = read_test_case('sorted')
	start = time.time()
	selection_sort(array_s)
	print('Time Sorted :', time.time() - start)
    
	print('')

	return array_u, array_s

def do_bubble_sort():
	print('Doing bubble sort :')

	array_u = read_test_case('unsorted')
	start = time.time()
	bubble_sort(array_u)
	print('Time Unsorted :', time.time() - start)
	
	array_s = read_test_case('sorted')
	start = time.time()
	bubble_sort(array_s)
	print('Time Sorted :', time.time() - start)

	print('')

	return array_u, array_s


def do_insertion_sort():
	print('Doing insertion sort :')

	array_u = read_test_case('unsorted')
	start = time.time()
	insertion_sort(array_u)
	print('Time Unsorted :', time.time() - start)

	array_s = read_test_case('sorted')
	start = time.time()
	insertion_sort(array_s)
	print('Time Sorted :', time.time() - start)
	
	print('')

	return array_u, array_s

def do_quick_sort():
	print('Doing Quick sort :')

	array_u = read_test_case('unsorted')
	start = time.time()
	quick_sort(array_u, 0, len(array_u) -1)
	print('Time Unsorted :', time.time() - start)

	#Not doing sorted case because pivot function is shit.
	#This will not work with sorted array.
	'''	array_s = read_test_case('sorted')
	start = time.time()
	quick_sort(array_s, 0, len(array_s) -1)
	print('Time Sorted :', time.time() - start)'''

	print('')

	return array_u

def do_merge_sort():
	print('Doing Merge sort :')

	array_u = read_test_case('unsorted')
	start = time.time()
	merge_sort(array_u, [0]*len(array_u), 0, len(array_u)-1)
	print('Time Unsorted :', time.time() - start)

	array_s = read_test_case('sorted')
	start = time.time()
	merge_sort(array_s, [0]*len(array_s), 0, len(array_s)-1)
	print('Time Sorted :', time.time() - start)
	
	print('')

	return array_u, array_s

if __name__ == '__main__':
	N = 10000
	generate_test_case(N)

	sol_python, sol_python_s  = do_python_sort()
	sol_select, sol_select_s = do_selection_sort()
	sol_bubble, sol_bubble_s = do_bubble_sort()
	sol_insertion, sol_insertion_s = do_insertion_sort()
	sol_quick = do_quick_sort()
	sol_merge, sol_merge_s = do_merge_sort()

	print('Checking if solutions are correct:')
	print(sol_python == sol_select == sol_bubble == sol_insertion == sol_quick == sol_merge)
	print(sol_python_s == sol_select_s == sol_bubble_s == sol_insertion_s == sol_merge_s)
