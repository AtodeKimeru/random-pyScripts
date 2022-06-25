number = int(input('choose a number: '))
epsilon = 0.001
least = 0.0
top = max(1.0, number)
answer = (top + least) / 2

while abs(answer**2 - number) >= epsilon:
    if answer**2 < number:
        least = answer
    else:
        top = answer
    
    answer = (top + least) / 2

answer = round(answer, 4)
print(f'The square root of {number} is {answer}')
