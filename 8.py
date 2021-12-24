def GCD(a: int, b: int):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


a, b = map(int, input().split())
min = int(GCD(a, b))
max = int(a * b / min)
print(min, max)


def isPrime(a: int):
    if a >= 2:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    return False


a = int(input())
print(isPrime(a))