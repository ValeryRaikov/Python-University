from math import sqrt

def check():
    try:
        number = float(input("Enter a number to calculate: "))

        if number <= 0:
            raise ValueError
        elif number % int(number) != 0:
            raise Exception
        else:
            new_num = sqrt(number)
            if new_num % int(new_num) != 0:
                raise Exception
            else:
                print("Sqrt is:", round(new_num))
            
    except ValueError:
        print("Square root of negative numbers is impossible!")
    except Exception:
        print("Error. The square root of this number is not exact!")
        
check()
        