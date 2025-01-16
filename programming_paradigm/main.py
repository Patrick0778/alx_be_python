import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[0]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
    safe_divide(1, 0)
    safe_divide(1, 'a')
    safe_divide(1, 2)