import numpy as np


def calculate_dental_metrics(measurements: list[float]) -> dict[str, float]:
    """
    Calculate average and maximum dental measurements.

    Args:
        measurements (list[float]): A list of dental measurement values.

    Returns:
        dict[str, float]: A dictionary with 'average' and 'max' keys containing the computed values.
            If the input list is empty, returns {'average': 0.0, 'max': 0.0}.

    Examples:
        >>> calculate_dental_metrics([1.0, 2.0, 3.0])
        {'average': 2.0, 'max': 3.0}

        >>> calculate_dental_metrics([])
        {'average': 0.0, 'max': 0.0}
    """

    if not measurements:
        return {"average": 0.0, "max": 0.0}

    return {"average": float(np.mean(measurements)), "max": float(np.max(measurements))}
