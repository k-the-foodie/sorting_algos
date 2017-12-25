def valid_int_array(array):

    """
    Input : list of values
    Note :
        Checks if all the entries in given array are integers
    Returns : Truth value

    """
    for i in array:
        if type(i) != int:
            return False
    return True


def selection_sort(array):
    
    """
    Input : list of values
    Note :
        Two parts of array are maintained, sorted part and unsorted part. Then algorithm will find the minimum of unsorted
        array and place it at the end of sorted array. This procedure is repeated until entire array is sorted.
    Returns : sorted list of values    
    
    """
    def find_min(array):
        
        """
        Input : list of values
        Returns : min of the array, pos of first occurence of min
        
        """
        
        minimum = None
        pos = None
        for i, element in enumerate(array):
            if minimum == None or element < minimum:
                minimum = element
                pos = i
                
        return minimum, pos
    
    for i in range(len(array)-1):
        # Currentlly sorted array length is i-1.
        _, pos = find_min(array[i:])
        # Returned position has index from array[i:], hence we need to add 'i' to get position in original array.
        pos += i
        array[i], array[pos] = array[pos], array[i]
        
    return array


def bubble_sort(array):
   
    """
    
    Input : list of values
    Note :
        Compares neighbouring elements and sortes them. Loops through the list multiple times until list is sorted.
    Returns : sorted list of values
    
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = False
    return array


def insertion_sort(array):
    
    """
    Input : list of values
    Note :
        Two parts of array are maintained, sorted part and unsorted part. Then algorithm will take first element of the unsorted
        array and finds it position in sorted array by comparing elements in it. Then same step will be repeated until entire
        array is sorted.
    Returns : sorted list of values    
    
    """
    for i in range(1, len(array)):
        new_position = i
        j = i-1
        while j >= 0:
            if array[j] > array[i]:
                new_position = j
            if array[j] <= array[i]:
                j = 0
            j -= 1
        array[new_position], array[new_position+1:i+1] = array[i], array[new_position:i]
    return array


def merge_sort(array):
    
    """
    Input : list of values
    Note :
        It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
    Returns : sorted list of values
    
    """
    
    def join_sorted_arrays(array1, array2):

        """
        Input : 2 sorted arrays.
        Returns : New sorted array

        """

        new_array = []    # this array will contain values from both input arrays.
        j = 0             # Index to keep track where we have reached in second array
        n2 = len(array2)
        
        for i, element in enumerate(array1):
            # We will compare current element in array1 to current element in array2, if element in array2 is smaller, append it
            # to new array and look at next element in array2. Keep doing this until either array2 is exhausted or an element of
            # array2 greater than current element of array1 is found.
            while j < n2 and element > array2[j]:
                new_array.append(array2[j])
                j += 1
            new_array.append(element)
        # If there are any remaining values in array2, that are bigger than last element in array1, then append those to 
        # new array.
        for i in range(j,n2):
            new_array.append(array2[i])
        return new_array
    
    n = len(array)
    if n == 1:
        return array
    else:
        array[:int(n/2)] = merge_sort(array[:int(n/2)])
        array[int(n/2):] = merge_sort(array[int(n/2):])
        array[:] = join_sorted_arrays(array[:int(n/2)],array[int(n/2):])
        return array


def quick_sort(array):
    
    """
    Input : list of values
    Note :
        picks an element as pivot and partitions the given array around the picked pivot, so that resulting position of pivot 
        is same as that in the sorted array. Then function will sort two subarrays viz., values to either side of the pivot.
    Output : sorted list of values.
    
    """
    
    def sort_around_pivot(array):
        
        """
        Input : list of values
        Note:
            picks last element as pivot. sorts the array such that, all elements to the left of the pivot are less than or equal
            to pivot and all elements to the right are strictly greater than pivot.
        Output : list of values
        
        """
        
        n = len(array)
        pivot = array[n-1]
        index_of_smaller_values = -1
        for i in range(n-1):
            if array[i] <= pivot:
                index_of_smaller_values += 1
                array[i], array[index_of_smaller_values] = array[index_of_smaller_values], array[i]
        # Now put pivot at its correct position
        pivot_pos = index_of_smaller_values+1
        array[n-1], array[pivot_pos] = array[pivot_pos], array[n-1]
        return pivot_pos
    
    if len(array) <= 1:
        return array
    else:
        pivot_pos = sort_around_pivot(array)
        array[:pivot_pos] = quick_sort(array[:pivot_pos])
        array[pivot_pos+1:] = quick_sort(array[pivot_pos+1:])
        return array


def heap_sort(array):
    
    """
    Input : list of values
    Note:
        Builds a max heap of given array. Then swaps first element (which is largest) of the array with the last, and heapifys 
        w.r.t new first element (array excluding the last element). It reapeats this procedure till array is sorted.
    Returns : sorted list of values
    
    """
    def max_heap(array):
        
        """
        Input : list of values
        Note: Builds max_heap by calling heapify function on all parent nodes.
        Returns : max_heap list of values
        
        """
        
        n = len(array)
        for i in range(int(n/2)-1,-1,-1):
            # We need to heapify parents only.
            # int(n/2) - 1 is highest index a parent node can have.
            array[:] = heapify(array, i)
        return array

    def heapify(array, index):
        
        """
        Input : list of values, index
        Note :
            element at given index is placed in the heap such that its parent is greater than or equal to it and its children are
            less than or equal to it.
        Returns : list of values
        
        """
        
        n = len(array)
        right_child_index = 2*(index+1)
        left_child_index = right_child_index - 1
        if right_child_index < n:
            max_child_index = right_child_index
            if array[left_child_index] > array[right_child_index]:
                max_child_index = left_child_index
            if array[index] < array[max_child_index]:
                array[index], array[max_child_index] = array[max_child_index], array[index]
                # If given element, in its new position, still has children, then we need to heapify again.
                if max_child_index <= int(n/2) - 1:
                    # given number is highest possible index a parent can have.
                    array[:] = heapify(array, max_child_index)
            return array
        elif left_child_index == n - 1:
            if array[index] < array[left_child_index]:
                array[index], array[left_child_index] = array[left_child_index], array[index]
            return array
        return array
    
    array[:] = max_heap(array)
    n = len(array)
    for i in range(n-1):
        array[0], array[n-1-i] = array[n-1-i], array[0]
        array[:n-1-i] = heapify(array[:n-1-i],0)
    return array


def counting_sort(array):
    
    """
    Input : list of integers
    Note:
        finds minimum and maximum elements, counts number of times each value has occured. Then loops through range(min,max) and 
        puts element in the array according to its count.
    Returns : sorted list of integers
    
    """
    
    if not valid_int_array(array):
        raise ValueError('Counting sort only accepts integer valued arrays.')

    counts = {}
    min_ele = None
    max_ele = None
    for element in array:
        if min_ele == None or element < min_ele:
            min_ele = element
        if max_ele == None or element > max_ele:
            max_ele = element
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    for i in range(counts[min_ele]):
        array[i] = min_ele
    running_count = [counts[min_ele]]
    # In the loop below, last entry of running_counts is used, hence it should contain at least one entry for first run of the
    # loop
    for i in range(min_ele + 1, max_ele+1):
        # max_ele has to be included, hence max_ele + 1.
        # Other option is to use range(min_ele+1, max_ele) and after the loop is finished, use counts_array.append(len(array))
        if i in counts:
            running_count.append(running_count[-1] + counts[i])
            for j in range(running_count[-2], running_count[-1]):
                array[j] = i
        else:
            running_count.append(running_count[-1])
            
    return array


def radix_sort(array):
    
    """
    Input : list of integers
    Note :
        Sorts elements by calling another sort method only on one digit at a time.
    Returns : sorted list of values
    
    """

    if not valid_int_array(array):
        raise ValueError('Radix sort only accepts integer valued arrays.')
    
    def custom_counting_sort(array, digit_place):
        
        """
        Input : list of values
        Note:
            sorts element based on values at given digits place.
        Returns : list of values
        
        """
        
        def extract_digit_at_given_place(number, digit_place):
            
            """
            Input : Integer
            Note :
                extracts digit at give place in the number.
            Returns : integer between 0 to 9 (both included)
            
            """
            try:
                return int(str(number)[-1-digit_place])
            except IndexError:
                return 0
        
        counts = {}
        for i in range(10):
            counts[i] = []
        # counts is a dictionary. Keys are 0, 1, 2, ..., 9. Associated values are empty lists. Elements in array will be stored
        # in these lists. Count for given key is simply length of the list associated with it.
        
        for i in range(len(array)):
            counts[extract_digit_at_given_place(array[i], digit_place)].append(array[i])
            
        running_count = 0
        for i in range(10):
            for j in range(len(counts[i])):
                array[running_count] = counts[i][j]
                running_count += 1
                
        return array
    
    max_ele = None
    for i in range(len(array)):
        if max_ele == None or array[i] > max_ele:
            max_ele = array[i]
            
    no_of_digits = len(str(max_ele))
    for i in range(no_of_digits):
        array[:] = custom_counting_sort(array, i)
        
    return array
