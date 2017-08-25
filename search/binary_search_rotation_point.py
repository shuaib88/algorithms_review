def rotation_point_of(word_array, left_index=0, right_index=None):
    if not right_index:
        right_index = len(word_array) - 1

    midpoint = (right_index + left_index)/2

    if right_index - left_index == 0:
        return midpoint

    if word_array[midpoint]>word_array[midpoint+1]:
        return midpoint

    else:
        if word_array[midpoint] > word_array[right_index]:
            return rotation_point_of(word_array,midpoint,right_index)
        else:
            return rotation_point_of(word_array,left_index,midpoint)

# test array
word_array = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
# word_array = [
#     'xenoepist',
#     'asymptote', # <-- rotates here!
# ]


#execute
# word_dict = known_word_dict(word_array)
# word_dict.rotation_point_of(word_array)
# print len(word_array)
print rotation_point_of(word_array,right_index=len(word_array)-1)
