n = int(input("Enter Number: "))

if n < 2:
    print("Please enter a number greater than or equal to 2")
else:
    count = 0
    i = 2

    while(i * i <= n):
        if n % i == 0:
            count = count + 1
        i = i + 1

    if count == 0:
        print(n, "is a Prime Number")
    else:
        print(n, "is not a Prime Number")


limit = int(input("\nEnter the limit: "))

if limit < 2:
    print("Invalid limit")
else:
    print("Prime numbers are:")

    for n in range(2, limit + 1):
        count = 0
        i = 2

        while(i * i <= n):
            if n % i == 0:
                count = count + 1
            i = i + 1

        if count == 0:
            print(n, end=" ")