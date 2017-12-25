import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-5] + 'sorting_algos')
# What is above line doing ?
# To import files from other directories, we need to add path to that file in sys.path
# os.path.dirname(os.path.realpath(__file__)) gives full path to current directory which ends in master_folder\tests.
# our required file is in folder named 'sorting_algos', and path is master_folder\sorting_algos.
# Hence we are dropping last 5 characters in generated path (i.e., 'tests') and adding 'sorting_algos' to path.
from sorting_algos import *

class test_valid_int_array(unittest.TestCase):

	"""
	testing a function which validates whether given array has all integers.

	"""

	def test_true_case(self):

		"""
		Integer array will be supplied to the function. Function should return True for it to pass the test.

		"""
		truth_value = valid_int_array([2,3,1,4])
		self.assertTrue(truth_value)

	def test_false_case(self):

		"""
		Array with non-integer values will be provided to function. It should return False to pass the test.

		"""
		truth_value = valid_int_array([2,5,2.3])
		self.assertFalse(truth_value)

class test_selection_sort(unittest.TestCase):

	"""
	Testing selection sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_numeric_array(self):

		"""
		Array containing int as well as float values will be given. To pass the test, returned array should be sorted.

		"""
		result = selection_sort([1,2.3,1.2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,1.2,2.3,5,6,23])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, returned array should be sorted alphabetically.

		"""
		result = selection_sort(['vf','acd','abcd','zaaaa','i'])
		self.assertEqual(result, ['abcd','acd','i','vf','zaaaa'])

class test_bubble_sort(unittest.TestCase):

	"""
	Testing bubble sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_numeric_array(self):

		"""
		Array containing int as well as float values will be given. To pass the test, returned array should be sorted.

		"""
		result = bubble_sort([1,2.3,1.2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,1.2,2.3,5,6,23])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, returned array should be sorted alphabetically.

		"""
		result = bubble_sort(['vf','acd','abcd','zaaaa','i'])
		self.assertEqual(result, ['abcd','acd','i','vf','zaaaa'])

class test_inserion_sort(unittest.TestCase):

	"""
	Testing insertion sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_numeric_array(self):

		"""
		Array containing int as well as float values will be given. To pass the test, returned array should be sorted.

		"""
		result = insertion_sort([1,2.3,1.2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,1.2,2.3,5,6,23])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, returned array should be sorted alphabetically.

		"""
		result = insertion_sort(['vf','acd','abcd','zaaaa','i'])
		self.assertEqual(result, ['abcd','acd','i','vf','zaaaa'])

class test_merge_sort(unittest.TestCase):

	"""
	Testing merge sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_numeric_array(self):

		"""
		Array containing int as well as float values will be given. To pass the test, returned array should be sorted.

		"""
		result = merge_sort([1,2.3,1.2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,1.2,2.3,5,6,23])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, returned array should be sorted alphabetically.

		"""
		result = merge_sort(['vf','acd','abcd','zaaaa','i'])
		self.assertEqual(result, ['abcd','acd','i','vf','zaaaa'])

class test_quick_sort(unittest.TestCase):

	"""
	Testing quick sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_numeric_array(self):

		"""
		Array containing int as well as float values will be given. To pass the test, returned array should be sorted.

		"""
		result = quick_sort([1,2.3,1.2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,1.2,2.3,5,6,23])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, returned array should be sorted alphabetically.

		"""
		result = quick_sort(['vf','acd','abcd','zaaaa','i'])
		self.assertEqual(result, ['abcd','acd','i','vf','zaaaa'])

class test_heap_sort(unittest.TestCase):

	"""
	Testing heap sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_numeric_array(self):

		"""
		Array containing int as well as float values will be given. To pass the test, returned array should be sorted.

		"""
		result = heap_sort([1,2.3,1.2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,1.2,2.3,5,6,23])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, returned array should be sorted alphabetically.

		"""
		result = heap_sort(['vf','acd','abcd','zaaaa','i'])
		self.assertEqual(result, ['abcd','acd','i','vf','zaaaa'])

class test_counting_sort(unittest.TestCase):

	"""
	Testing counting sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_int_array(self):

		"""
		Array containing int values will be given. To pass the test, returned array should be sorted.

		"""
		result = counting_sort([1,2,2,1,0,5,23,6])
		self.assertEqual(result, [0,1,1,2,2,5,6,23])

	def test_float_array(self):

		"""
		Array containing float values will be given. To pass the test, function should raise valueerror.

		"""
		self.assertRaises(ValueError, counting_sort, [[0,1.2,1,2,2,5,6,23]])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, function should raise valueerror.

		"""
		self.assertRaises(ValueError, counting_sort, [['abcd','acd','i','vf','zaaaa']])

class test_radix_sort(unittest.TestCase):

	"""
	Testing radix sort. Will be tested with numeric and non-numeric arrays.

	"""

	def test_int_array(self):

		"""
		Array containing int values will be given. To pass the test, returned array should be sorted.

		"""
		result = radix_sort([111111,25,562,100,0,55,23,6])
		self.assertEqual(result, [0,6,23,25,55,100,562,111111])

	def test_float_array(self):

		"""
		Array containing float values will be given. To pass the test, function should raise valueerror.

		"""
		self.assertRaises(ValueError, radix_sort, [[0,1.2,1,2,2,5,6,23]])

	def test_non_numeric_array(self):

		"""
		Array containing strings will be given. To pass the test, function should raise valueerror.

		"""
		self.assertRaises(ValueError, radix_sort, [['abcd','acd','i','vf','zaaaa']])

if __name__ == '__main__':
	unittest.main()
