def fibo_sequence(n):
    fibo_series = []
    a = 0
    b = 1

    for i in range(n):
        fibo_series.append(a)
        a, b = b, a + b  

    return fibo_series

n = int(input("Enter the number of terms for the Fibonacci sequence: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibo_series = fibo_sequence(n)
    print("Fibonacci Sequence:")
    print(fibo_series)
