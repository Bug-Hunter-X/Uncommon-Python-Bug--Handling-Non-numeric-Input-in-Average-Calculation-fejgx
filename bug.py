def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)