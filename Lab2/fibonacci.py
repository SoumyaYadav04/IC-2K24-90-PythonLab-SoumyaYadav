def fib(n):
    a = 0
    b = 1

    print("Fibonacci using loop:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


count = 0

def fib_rec(n):
    global count
    count = count + 1

    if n <= 1:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)


n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    fib(n)

    print("\nFibonacci using recursion:")

    count = 0

    for i in range(n):
        print(fib_rec(i), end=" ")

    print("\nRecursive function calls:", count)