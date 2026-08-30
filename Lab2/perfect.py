n = int(input("Enter Number: "))

if n <= 0:
    print("Please enter a positive number")
else:
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        print(n, "is a Perfect Number")
    else:
        print(n, "is not a Perfect Number")


limit = int(input("\nEnter the limit: "))

if limit <= 0:
    print("Invalid limit")
else:
    print("Perfect numbers are:")

    for n in range(1, limit + 1):
        sum = 0

        for i in range(1, n):
            if n % i == 0:
                sum = sum + i

        if sum == n:
            print(n, end=" ")