while True:
    try:
        n = int(input("Enter number n: "))
        if n <= 0:
            raise Exception
        else:
            break
    except Exception:
        print("Number n must be positive!")
        
k = int(input("Enter number k: "))

list_one = []
list_alpha = []
list_beta = []

#list one
for num in range(n):
    number = int(input("Enter number: "))
    list_one.append(number)
    
print("Original list:", list_one)
    
# list alpha
for a in list_one:
    if a > k:
        list_alpha.append(a)
        
print("New list alpha:", list_alpha)

multiplication = 1
for index in range(len(list_alpha)):
    if index % 2 != 0:
        multiplication *= list_alpha[index]
        
print("Multiplication is:", multiplication)

if len(list_alpha) > 0:
    i_min = list_alpha.index(min(list_alpha))
    print("Min index is:", i_min)
else:
    print("No numbers in the list!")

#list beta
for b in list_one:
    if b > 0 and b <= k:
        list_beta.append(b)
        
print("New list beta:", list_beta)

max_beta = max(list_beta)
min_beta = min(list_beta)
if len(list_beta) > 1: 
    diff = max_beta - min_beta
    print("Difference in list beta is:", diff)
else:
    print("Not enough numbers to find the difference!")