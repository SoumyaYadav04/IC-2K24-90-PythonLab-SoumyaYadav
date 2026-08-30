n = int(input("Enter Number: "))

if n < 0:
    print("Please enter a non-negative number")
else:
    sum = 0
    order = len(str(n))
    copy_n = n

    while(n > 0):
        digit = n % 10
        sum = sum + digit ** order
        n = n // 10

    if sum == copy_n:
        print(copy_n, "is an Armstrong Number")
    else:
        print(copy_n, "is not an Armstrong Number")


start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

if start < 0 or start > end:
    print("Invalid range")
else:
    print("Armstrong numbers are:")

    for n in range(start, end + 1):
        sum = 0
        order = len(str(n))
        copy_n = n

        while(n > 0):
            digit = n % 10
            sum = sum + digit ** order
            n = n // 10

        if sum == copy_n:
            print(copy_n, end=" ")