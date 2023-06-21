from functools import reduce

while True:
    num = input("Enter your ratio: ")
    try: 
        n = int(num) 
        if n <= 0 or n > 100:
            raise Exception
        
        break
    except ValueError:
        print("Invalid user operation!")
    except Exception:
        print("Invalid ratio entered!")    

all_numbers = []
for _ in range(n):
    while True:
        num = input("Enter a number: ")
        try:
            number = int(num)
            all_numbers.append(number)
            break
        except ValueError:
            print("Please enter an integer!")
            
print(f"All numbers are: {all_numbers}")
        
list_alpha = [x for x in all_numbers if x % 2 != 0 and x % 3 == 0]
print(f"List alpha is: {list_alpha}")
list_beta = [y for y in all_numbers if y % 2 == 0]
print(f"List beta is: {list_beta}")

if len(list_alpha) >= 2:
    print(f"Max number in list_alpha is: {max(list_alpha)}")
    print(f"Min number in list_alpha is: {min(list_alpha)}")
else:
    print("The list is empty or does not contain enough numbers!")
    
if len(list_beta) >= 1:
    addition = reduce(lambda a, b: a + b, list_beta)
    print(f"The sum is: {addition}")
    
    avg = addition / len(list_beta)
    print(f"Average sum is: {avg}")
else:
    print("The list is empty!")
    
#Again there are plenty of methods to solve his problem. It is a matter of choice how to do it.