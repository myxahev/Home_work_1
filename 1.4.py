number = int(input('input number: '))
largest_number = 0
while number != 0:
    last_digit = number % 10
    if last_digit > largest_number:
        largest_number = last_digit
    number = number // 10
print(f'largest number = {largest_number}')