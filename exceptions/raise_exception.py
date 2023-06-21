try:
    num_1 = float(input())
    num_2 = float(input())

    if num_2 == 0:
        raise Exception
except TypeError:
    print("Invalid type for num!")
except Exception:
    print("Cannot divide by zero!")
else:
    result = num_1 / num_2
    print("Result is",result)
finally:
    print("Done!")