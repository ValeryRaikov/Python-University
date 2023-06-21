from functools import reduce

numbers = []

while True:
    num = input("Enter number: ")
    try:
        number = int(num)
        
        if number == 0:
            break
        
        numbers.append(number)
    except ValueError:
        print("Invalid user input!")
    
print(f"All numbers are: {numbers}")

list_alpha = [x for x in numbers if x % 3 == 0 and x % 2 == 0]
print(f"List alpha is: {list_alpha}")

if len(list_alpha) >= 1:
    odd_list = [list_alpha[i] for i in range(len(list_alpha)) if i % 2 != 0]
    print(f"Odd list is: {odd_list}")
    
    addition = reduce(lambda x, y: x + y, odd_list)
    
    print(f"The sum is: {addition}")
else:
    print("The list is empty!")

list_beta = [y for y in numbers if y % 7 == 0 and y % 2 != 0]
print(f"List beta is: {list_beta}")

if len(list_beta) >= 2:
    print(f"Sorted list is: {sorted(list_beta, reverse = True)}")

    prod = min(list_beta) * max(list_beta)
    print(f"Product is: {prod}")
else:
    print("The list is empty or does not have enough components!")