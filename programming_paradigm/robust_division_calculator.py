def safe_divide(numerator, denominator, default=None):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        print(f"The result of division is {num / den}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return default
    except (ValueError):
        print("Error: Please enter numeric values only.")