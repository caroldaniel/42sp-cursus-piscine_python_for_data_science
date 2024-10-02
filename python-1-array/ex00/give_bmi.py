import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
Calculate BMI from height and weight.

Parameters:
    height: list of int or float, height in meters
    weight: list of int or float, weight in kilograms

Returns:
    list of int or float, BMI values
"""

    # Convert lists to numpy arrays
    height = np.array(height)
    weight = np.array(weight)

    # Error handling
    if height.shape != weight.shape:
        return []
    if not (np.issubdtype(height.dtype, np.number) and
            np.issubdtype(weight.dtype, np.number)):
        return []

    # Calculate bmi
    bmi = weight / (height ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Apply a limit to a list of BMI values.

Parameters:
    bmi: list of int or float, BMI values
    limit: int, limit value

Returns:
    list of bool, True if BMI is above limit, False otherwise
"""
    return (np.array(bmi) > limit).tolist()
