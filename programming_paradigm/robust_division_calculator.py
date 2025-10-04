
def safe_divide(numerator, denominator):
    try:
        nume = float(numerator)
        den = float(denominator)

        try:
            result = nume / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

























    # division = float(numerator / denominator)
    # try:
    #     if denominator != 0:
    #         print (f"The result of the division is {division}")
    # except ZeroDivisionError:
    #     print("Error: Cannot divide by zero.")
    #
    # except ValueError:
    #     print("Error: Please enter numeric values only.")

