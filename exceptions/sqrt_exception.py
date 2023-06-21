import math

def check(number):
    
    try: 
        if number <= 0:
            raise ValueError
        result = math.sqrt(number)
    except ValueError:
        result = "This is a negative root! Try again."
    except TypeError:
        result = "This is a string! Try again."
    except:
        result = "Unexpected error! Try again."
    finally:
        print("Done!")
    
    print("Output:", result)
    
check(number = float(input()))