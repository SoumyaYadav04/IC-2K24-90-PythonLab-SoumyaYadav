Python Lab 2
1. Armstrong Number
Aim
To check whether a number is an Armstrong number and find Armstrong numbers in a given range.
Logic
First, I find the number of digits and calculate the sum of each digit raised to that power. Then I compare the sum with the original number.

Sample Input / Output
Input: 153
Output: 153 is an Armstrong Number
Range: 100 to 1000
Output: 153 370 371 407

2. Prime Number
Aim
To check whether a number is prime and print prime numbers up to a given limit.
Logic
I check the divisors of the number. If it has only two divisors, 1 and itself, then it is a prime number.

Sample Input / Output
Input: 7
Output: 7 is a Prime Number
Limit: 20
Output: 2 3 5 7 11 13 17 19

3. Perfect Number
Aim
To check whether a number is a perfect number and find perfect numbers up to a given limit.
Logic
I find all the proper divisors of the number and add them. If the sum is equal to the number, it is a perfect number.

Sample Input / Output
Input: 28
Output: 28 is a Perfect Number
Limit: 100
Output: 6 28

4. Palindrome
Aim
To check whether a number and a string are palindromes.
Logic
For the number, I reverse it using arithmetic operations and compare it with the original number. For the string, I compare the string with its reverse.

Sample Input / Output
Input: 121
Output: Number palindrome
Input: madam
Output: String palindrome

5. Fibonacci Series
Aim
To print the Fibonacci series using a loop and recursion and count the recursive function calls.
Logic
In the loop method, I use three variables to calculate the next term. In the recursive method, the function calls itself to find the previous two terms.

Sample Input / Output
Input: 10
Output:
0 1 1 2 3 5 8 13 21 34
Recursive function calls: 177

6. Pattern Printing
Aim
To print different patterns using nested loops.
Logic
I use nested for loops to print the required number of rows and columns. Spaces are used before the stars to make the pyramid pattern.

Sample Input / Output
Input: 4
Output:

Star Pattern
*
* *
* * *
* * * *

Number Pattern
1
1 2
1 2 3
1 2 3 4

Pyramid Pattern
*
* * *
* * * * *
* * * * * * *

7. Menu-Driven Application
Aim
To combine programs 1 to 6 using a menu-driven program.
Logic
The program displays different options in a menu. According to the choice entered by the user, the required operation is performed and the menu is shown again.

Sample Input / Output
Input: 2
Enter Number: 7
Output: Prime Number
Input: 7
Output: Program ended.

8. Number Guessing Game
Aim
To make a number guessing game using a random number.
Logic
The program generates a random number between 1 and 100. The user gets 7 attempts and is told whether the guess is too high, too low or correct.

Sample Input / Output
Input: 50, 75, 63
Output:
Too low
Too high
Correct!
Attempts taken: 3

Analysis
1. For Loop and While Loop
I used for loop when the number of repetitions was known, like in Fibonacci, patterns and ranges. I used while loop when the condition had to be checked repeatedly, like reversing a number.

2. Fibonacci Loop and Recursion
The recursive version repeats more work as n increases because the same values are calculated again and again. The loop version is faster because it calculates each term only once.

3. Prime Number Check
We only need to check divisors up to the square root of the number. If a number has a divisor greater than its square root, there will always be another divisor smaller than the square root.

4. Number Guessing Game
The strategy is called Binary Search. We guess the middle value of the remaining range each time, which reduces the possible numbers by half.
