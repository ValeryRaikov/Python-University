import random

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
    number = random.randrange(20, 600)
    all_numbers.append(number)
    
print(f"List with all numbers: {all_numbers}")

list_alpha = [a for a in all_numbers if a % 2 == 0]
print(f"Even numbers are: {list_alpha}")

list_beta = []
for num in all_numbers:
    if (num % 10) % 5 == 0 or (num % 100) % 5 == 0:
        list_beta.append(num)
        
print(f"List beta is: {list_beta}")

list_beta = [a for a in list_alpha + list_beta]
print(list_beta)