def ft_filter(function, iterable):
    """
    Mimics Python's built-in filter() using list comprehension.

    Parameters:
        function: A function that returns True or False.
        iterable: An iterable to filter.

    Returns:
        A filter object (like the built-in filter()).
    """
    if function is None:
        return (item for item in iterable if item)

    return (item for item in iterable if function(item))
