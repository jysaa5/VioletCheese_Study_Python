# 10872번: 팩토리얼
number = int(input())


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(number))