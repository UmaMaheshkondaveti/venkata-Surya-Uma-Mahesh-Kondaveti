def generate_sequence(x):
    result = []
    current = 1
    count = 0
    while count < x:
        result.append(current)
        current += 2
        count += 1
    return result

num = int(input("Enter a number: "))
seq = generate_sequence(num)
print(", ".join(map(str, seq)))
