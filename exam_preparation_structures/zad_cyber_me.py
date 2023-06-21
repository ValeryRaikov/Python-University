while True:
    try:
        n = int(input("Enter number for n: "))
        
        if n < 30 or n > 100:
            raise Exception
        
        break
    except ValueError:
        print("Wrong user input! Integer needed.")
    except Exception:
        print("N must be between 30 and 100!")
    
all_numbers = [] 
        
for _ in range(n):
    while True:
        try:
            number = int(input("Enter number: "))
            all_numbers.append(number)
            
            break
        except ValueError:
            print("Wrong user input! Integer needed.")
    
print(f"List with all numbers: {all_numbers}")