numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

for i in range(1, len(numbers) + 1):
    print(f"{i} --> {numbers[i-1]}")
    
for i in range(1, len(numbers) + 1):
    print(i)
    
for i in numbers:
    print(i)
    
for a, b in enumerate(numbers, 1):
    if a % 2 != 0:
        print(f"{a} --> {b}")
        
divided_by_3 = map(lambda x: int(x / 3), numbers)
print(list(divided_by_3))
again = [x / 3 for x in numbers]
print(again)