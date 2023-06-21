try:
    age = float(input("Enter your age: "))
    if type(age) == float:
        raise FloatingPointError
    
    age_int = int(age)
    
    if age_int < 0 or age_int > 100:
        raise Exception
except FloatingPointError:
    print("Age should be a whole number!")
except Exception:
    print("Invalid age value!")