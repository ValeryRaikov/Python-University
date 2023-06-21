nums = [4, 5, 6, 7]
factoreil_of_nums = []

for num in nums:
    current_num = num
    factoriel = 1
    
    while current_num > 0:
        factoriel *= current_num
        current_num -= 1
        
    factoreil_of_nums.append(factoriel)    

print(f"The list of factoriels: {factoreil_of_nums}")