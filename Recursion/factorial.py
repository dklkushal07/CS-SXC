# for finding factorial, formula is n! = n * (n-1)

def factorial(number):
    # for 0, 0! = 1
    if number == 0:
        answer = 1
    else:
        answer = number * factorial(number - 1)
    return answer


print("The factorial is",factorial(int(input("Enther the number you want the factorial of"))))
