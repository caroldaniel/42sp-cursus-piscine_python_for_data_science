import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
Slice a list from start to end after printing its shape.

Parameters:
    family: list, a list of family members
    start: int, start index

Returns:
    list, a slice of the list from start to end
"""

    # Convert the input list to a NumPy array
    try:
        family_array = np.array(family)
    except Exception as e:
        raise ValueError(f"Error converting list to NumPy array: {e}")

    # Error handling: check if it's a 2D array
    if family_array.ndim != 2:
        raise ValueError("Input must be a 2D list.")

    # Print the shape of the original array
    print(f"My shape is : {family_array.shape}")

    # Apply slicing
    truncated_family = family_array[start:end]

    # Print the shape of the truncated array
    print(f"My new shape is : {truncated_family.shape}")

    # Return the truncated array as a list
    return truncated_family.tolist()
