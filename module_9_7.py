def is_prime(func):
    def wrapper(first, second, third):
        result = func(first, second, third)
        for i in range(2, result):
            if result == 1:
               number = 'Число ни простое, ни составное'
            elif result % i == 0:
                number = 'Составное'
                break
            else:
                number = 'Простое'

        return f'{number}\n{result}'
    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third

result = sum_three(2 , 3, 6)
print(result)
