def ePalindromo(num):
    n = num
    x = 0
    while n > 0:
        x = (x * 10) + (n % 10)
        n = n // 10

    return x == num

print(ePalindromo(1213))
