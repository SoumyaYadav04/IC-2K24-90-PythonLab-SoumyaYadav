number = int(input("Enter Number: "))

if number < 0:
    print("Please enter a non-negative number")
else:
    temp = number
    reverse = 0

    while(number > 0):
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if temp == reverse:
        print("Number palindrome")
    else:
        print("Number not a palindrome")


string = input("\nEnter String: ")

reverse_string = string[::-1]

if string == reverse_string:
    print("String palindrome")
else:
    print("String not a palindrome")