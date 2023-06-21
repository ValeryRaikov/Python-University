while True:
    try:
        num_n = int(input("Enter number n: "))
    
        if num_n <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        print(f"Number n must be positive!")
    except:
        print("Unexpected error!")   

num_k = int(input("Enter number k: "))

x_nums = []
for i in range(1, num_n + 1):
    num_x = int(input(f"{i} --> Enter number: "))
    x_nums.append(num_x)

list_alpha = [x for x in x_nums if x > num_k]
print(f"List of nums is: {list_alpha}")

if len(list_alpha) > 0:
    prod = 1
    for a in range(1, len(list_alpha) + 1, 2):
            prod *= list_alpha[a - 1]
    print(f"Product is {prod}")
    
    print(f"Min num index is: {list_alpha.index(min(list_alpha))}")
else:
    print("No numbers in this list!")

list_beta = [y for y in x_nums if y <= num_k and y > 0]
print(f"List of nums is: {list_beta}")

if len(list_beta) > 0:
    print(f"Biggest number is: {max(list_beta)}")
    print(f"Smallest number is: {min(list_beta)}")
    diff = max(list_beta) - min(list_beta)
    print(f"Difference between biggest and smallest number is: {diff}")