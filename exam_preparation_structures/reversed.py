number = input("Enter number: ")
reversed_number = number[::-1]

if reversed_number == number:
    print(f"{number} is a palindorm.")
else:
    print(f"{number} is not a palindorm.")
    
######################################################################
# This doesn't work??? 
num = int(input("Enter number: "))
reversed_num = []
new_num = num

while num != 0:
    last_digit = new_num % 10
    reversed_num.append(last_digit)
    
    num %= 10
    new_num = num
    
reversed_num_str = "".join(reversed_num)

if reversed_num_str == str(num):
    print(f"{num} is a palindorm.")
else:
    print(f"{num} is not a palindorm.")