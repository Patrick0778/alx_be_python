def safe_divide(numerator, denominator, default=None):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return num / den
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return default
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return default