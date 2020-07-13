import collections
from itertools import groupby


# Create groups of characters in original string
def get_char_groups(user_string):
    char_list = list(user_string)
    util_func = lambda x: str.lower(x)
    temp = sorted(char_list, key=util_func)
    result_groups = [list(char) for i, char in groupby(temp, util_func)]
    return result_groups


# Sort string based on character frequency & order
def sort_string(user_string):

    # Get character groups
    string_group_buckets = get_char_groups(user_string)

    # Initialize variable
    first_non_repeating = None

    # Determine the frequency of each character.
    counts = collections.Counter(user_string.lower())
    max_freq = max(counts.values())

    # Find the first non-repeating character
    for key, val in counts.items():
        if val == 1:
            first_non_repeating = key
            break

    # Bucket sort the characters by frequency.
    buckets = [[] for _ in range(max_freq + 1)]
    for char, value in counts.items():
        buckets[value].append(char)

    # Build up the string.
    string_builder = []
    for i in range(0, len(buckets)):
        for chars in buckets[i]:
            string_builder.append(chars * i)

    answer_string = "".join(string_builder)

    # Loop each character grouping to replace(original string case) in sorted string
    for item in string_group_buckets:
        check_string = ''.join(item)
        if check_string.lower() in answer_string:
            answer_string = answer_string.replace(check_string.lower(), check_string)

    # Return results if string has non-repeating character
    if first_non_repeating:
        return first_non_repeating, answer_string
    else:
        return "No non-repeating characters", "No modification done"


# Get String from User
string = input('Enter a String: ')
# Format string as required
first_char, answer_string = sort_string(string)
# Display Results
print('First Non-Repeating Character is: ' + first_char)
print('Modified and Ordered String is: ' + answer_string)
