while True:
    try:
        n = int(input("Enter number n: "))
        if n <= 0:
            raise ValueError
        if type(n) != int:
            raise TypeError
        else:
            break
    except ValueError:
        print("Number must be positive!")
        continue
    except TypeError:
        print("Not an integer!")
        continue

print(f"Number n is: {n}")