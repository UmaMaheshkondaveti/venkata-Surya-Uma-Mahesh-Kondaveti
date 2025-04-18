def count_divisible_numbers(numbers):
    result = {}
    
    for i in range(1, 10):
        counter = 0
        
        for num in numbers:
            if num % i == 0:
                counter = counter + 1
        
        result[i] = counter
    
    return result

print("Enter some numbers separated by commas:")
user_input = input()

numbers = []
for item in user_input.split(","):
    numbers.append(int(item))

answer = count_divisible_numbers(numbers)

print(answer)
