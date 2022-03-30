"""
(c) 2022 Shoshi (Sharon) Cooper.  No duplication is permitted for commercial use.  Any significant changes made must be
stated explicitly and the original source code, if used, must be available and credited to Shoshi (Sharon) Cooper.

A sorting algorithm I came up with that allows you to use binary search.

It's very helpful if you do not start with a list, but instead are adding objects one by one into a list over time -- 
and you just want to know where to put them.  The "get_insertion_index" function is quite useful for this because it 
doesn't actually modify the list.  It just tells you where the new item is supposed to go, and it does so quickly.
"""


def binary_insert_sort_unsorted_list(lst, key=lambda x: x):
    """
    This is the function for if you begin with an entire unsorted list.  This function will modify the list 
    in-place so that it is sorted.
    """
    for i in range(1, len(lst)):
        new_index = get_insertion_index(lst, lst[i], end=i - 1, key=key)
        elem = lst.pop(i)
        lst.insert(new_index, elem)


def get_insertion_index(lst, new_obj, end: int = None, key=lambda x: x):
    """
    For adding an unordered element to an ordered (or empty) list.  Does this using binary search.
    The list is NOT modified by this function!  Instead, the correct insertion index is returned.

    Useful if you're adding items one by one to a list and want to just get the insertion index quickly.
    Kind of a Python-thing because it takes advantage of the extra memory space Python gives us inside its lists.
    That allows us to quickly pop and insert elements.

    :param lst: the list you are inserting into
    :param new_obj: the new object you are inserting
    :param end: the ending index of your list, if applicable.  Otherwise, ending index is assumed.
    :param key: A lambda function that tells which parameter or attribute you are using to compare elements during
        the sort.

    :return: the index at which the new item should be inserted so that the list will continue to be in order
    """

    # Set end and start
    start = 0
    if end is None:
        end = len(lst) - 1


    while True:
        # base cases: --> append to list (start > end) or prepend to list (end < 0)
        if end < 0 or start > end:
            return start

        middle = (end + start) // 2
        # Commentary on line below:
        #    Unoptimized, the line below would be: "if key(lst[middle - 1]) < key(new_num) < key(lst[middle])"
        #    The remainder of the line is for optimizations/conceptual clarity
        #
        #       > "or key(lst[middle]) == key(new_obj)" : an optimization for lists w/ lots of duplicate values
        #       > "if middle > 0" : this is really for conceptual accuracy.
        #           If middle == 0, then (middle - 1) = -1.  B/c lst is sorted, lst[-1] will always be >= lst[0],
        #           which means you don't actually need the "if middle > 0" b/c you'll get the same result without it.  
        #           However, it's conceptually incorrect to compare an element at the beginning of the list to the
        #           end of the list (and in other languages, there is no negative indexing).  So while this might
        #           get same result in Python, it's still clearer from a conceptual standpoint to specify.
        #           This is the reason that the line below starts with "if middle > 0".

        if middle > 0 and key(lst[middle - 1]) < key(new_obj) < key(lst[middle]) or key(lst[middle]) == key(new_obj):
            return middle

        elif key(new_obj) < key(lst[middle]):
            end = middle - 1
        else:
            start = middle + 1

