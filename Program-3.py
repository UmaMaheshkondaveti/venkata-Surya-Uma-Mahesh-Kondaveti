def generate_sequence(x):
    # If x is even, reduce it by 1
    if x % 2 == 0:
        x = x - 1
    
   
    result = []
    current = 1
    while current <= x:
        result.append(current)
        current += 2
    
    return result


num = int(input("Enter a number: "))


seq = generate_sequence(num)
if seq:
    print(", ".join(map(str, seq)))
else:
    print("No sequence for this input")
