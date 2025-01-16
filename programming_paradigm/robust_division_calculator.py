def safe_divide(numerator, denominator, default=None):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return numerator / denominator
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return default
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return default