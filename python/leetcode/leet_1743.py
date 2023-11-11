"""
NOT WORKING
"""


import numpy as np

def restore_array(adjacent_pairs):

    # Convert the list into a numpy array
    numpy_array = np.array(adjacent_pairs)

    # Create a dictionary to store the frequency and the index of each element
    element_dict = {}
    for i, pair in enumerate(numpy_array):
        for element in pair:
            if element not in element_dict:
                element_dict[element] = [1, i] # frequency and index
            else:
                element_dict[element][0] += 1 # increment frequency

    # Find the elements that occurred only once in the flattened array
    unique_elements = [element for element, value in element_dict.items() if value[0] == 1]

    # Check if there are no unique elements
    if not unique_elements:
        return [] # or return a message

    # Find the index of the list which has those elements
    unique_index = [element_dict[element][1] for element in unique_elements]

    result_list = [0] * len(adjacent_pairs)
    result_list[0] = unique_index[0]
    result_list[-1] = unique_index[-1]

    # Use a loop to find the next pair that matches the current pair
    current_pair = adjacent_pairs[result_list[0]]
    for i in range(1, len(adjacent_pairs) - 1):
        next_element = current_pair[1] # the second element of the current pair
        next_index = element_dict[next_element][1] # the index of the next pair
        result_list[i] = next_index
        current_pair = adjacent_pairs[next_index]

    return result_list