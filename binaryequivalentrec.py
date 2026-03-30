def binaryequivalentrec(n):
    if n > 1:
        binaryequivalentrec(n // 2)
    print(n % 2, end="")

n = int(input("Enter a number: "))
binaryequivalentrec(n)
