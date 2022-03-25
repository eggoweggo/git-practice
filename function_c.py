def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    new_set = set()
    set_a = set(list_a)
    set_b = set(list_b)

    new_set = set_a.union(set_b)

    return new_set


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
