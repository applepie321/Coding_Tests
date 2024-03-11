# Custom Sort String
# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

def custom_sort_string(order, s):
    """
    Returns a permutation of string s that satisfies the custom order given in order.

    Args:
        order (str): The custom order string.
        s (str) : The string to be permuted.

    Returns:
        str: A permutation of s that satisfies the custom order.
    """

    # Create a dictionary to store the count of each character in s
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    result = ""

    # First, append the character that are present in order
    for char in order:
        result += char * char_count.get(char, 0)
        # Remove the characters that are already added to the result
        char_count.pop(char, None)

    for char, count in char_count.items():
        result += char * count

    return result
