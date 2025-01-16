def safe_divide(numerator, denominator, default =0):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return f"The result of the division is {num / den}"
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return default
    except (ValueError):
        print("Error: Please enter numeric values only.")