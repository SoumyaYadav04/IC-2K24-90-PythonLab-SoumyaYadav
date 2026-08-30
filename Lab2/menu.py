def armstrong(n):
    total = 0
    temp = n
    order = len(str(n))

    while n > 0:
        digit = n % 10
        total = total + digit ** order
        n = n // 10

    if total == temp:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


def prime(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")


def perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


def palindrome(n):
    temp = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if temp == reverse:
        print("Number palindrome")
    else:
        print("Number not a palindrome")


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


def patterns(n):
    print("\nStar Pattern")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    print("\nNumber Pattern")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\nPyramid Pattern")

    for i in range(1, n + 1):
        print(" " * (n - i), end="")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


while True:

    print("\n----- MENU -----")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter Number: "))
        armstrong(n)

    elif choice == 2:
        n = int(input("Enter Number: "))
        prime(n)

    elif choice == 3:
        n = int(input("Enter Number: "))
        perfect(n)

    elif choice == 4:
        n = int(input("Enter Number: "))
        palindrome(n)

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        fibonacci(n)

    elif choice == 6:
        n = int(input("Enter number of rows: "))
        patterns(n)

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice")