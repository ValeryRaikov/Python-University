from functools import reduce

all_numbers = []

while True:
    try:
        num_n = input("Enter number for n: ")
        number_n = int(num_n)
        
        if number_n <= 0:
            raise Exception
        
        num_k = input("Enter number for k: ")
        number_k = int(num_k)
        
        break
    except ValueError:
        print("Invalid user input! Try again.")
    except Exception:
        print("N must be positive!")
        
for _ in range(number_n):
    while True:
        num_x = input("Enter number for x: ")
        
        try:
            number_x = int(num_x)
            all_numbers.append(number_x)
            break
        except ValueError:
            print("Invalid user input! Try again.")
   
print(f"All numbers are: {all_numbers}") 

list_alpha = [a for a in all_numbers if a % 2 == 0 and a % 5 == 0]
list_beta = [b for b in all_numbers if b % 2 == 1 and b % 3 == 0]
list_gama = [c for c in all_numbers if c % 7 == 0 or (c + 7) % 4 == 0]

print(f"List alpha is: {list_alpha}")        
print(f"List beta is: {list_beta}") 
print(f"List gama is: {list_gama}") 

new_list_numbers = set(list_alpha + list_beta + list_gama)
print(f"Combined list is: {list(new_list_numbers)}")

list_delta = [d for d in new_list_numbers if d > 0 and d <= number_k]
print(f"List delta is: {list_delta}")

if len(list_alpha) >= 2:
    print(f"Max number of list alpha is: {max(list_alpha)}")
    print(f"Min number of list alpha is: {min(list_alpha)}")
    print(f"Difference between max and min is: {max(list_alpha) - min(list_alpha)}")
else:
    print("More numbers needed!")
    
if len(list_beta) >= 2:
    print(f"Sorted list beta is: {sorted(list_beta, reverse = True)}")
    print(f"Max number index of list beta is {list_beta.index(max(list_beta))}")
    print(f"Min number index of list beta is {list_beta.index(min(list_beta))}")
else:
    print("More numbers needed!")
 
if len(list_gama) >= 2:
    sum_even = 0
    sum_odd = 0
    for i in range(len(list_gama)):
        if i % 2 == 0:
            sum_even += list_gama[i]
        elif i % 2 == 1:
            sum_odd += list_gama[i]
        else:
            print("Oops, something went wrong!")
        
    print(f"Sum of even numbers in list gama is: {sum_even}")
    print(f"Sum of odd numbers in list gama is: {sum_odd}")
else:
    print("More numbers needed!")
    
if len(list_delta) >= 2:
    sum_list_delta = reduce(lambda x, y: x + y, list_delta)
    sub_list_delta = reduce(lambda x, y: x - y, list_delta)
    
    print(f"The sum of list delta is: {sum_list_delta}")
    print(f"The sub of list delta is: {sub_list_delta}")
    
    squared_nums = list(map(lambda x: x ** 2, list_delta))
    print(f"Squared list is: {squared_nums}")
else:
    print("More numbers needed!")