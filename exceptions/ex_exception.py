import math

def function(num):
    try:
        result = math.sqrt(num)
    except:
        result = "Error"
        
    return result

while True:
    print(function(num = float(input())))