def odd_seq(n):
    result = []
    num = 1
    
    for i in range(n):
        result.append(num)
        num += 2
        
    return result

x = int(input("Enter a number: "))
sequence = odd_seq(x)
print(", ".join(map(str, sequence)))
