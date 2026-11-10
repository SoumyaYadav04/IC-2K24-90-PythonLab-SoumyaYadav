Lab 3: Concentric Number and Star Patterns

This lab focuses on generating concentric number patterns and different star patterns using Python loops and functions.

Programs

1. number_pattern.py

Aim: To print a concentric number square pattern based on a positive integer entered by the user.

Logic:

- Take a positive integer as input and calculate the size of the square.
- Use nested loops to calculate the minimum distance of each position from the edges.
- Subtract this distance from the input number to generate the concentric number pattern.

Sample Input:

Enter the number: 3

Sample Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3

---

2. pattern_matching.py

Aim: To generate different solid, triangular, diamond, and hollow star patterns using Python functions and loops.

Logic:

- Define separate functions for each star pattern using loops.
- Use string multiplication and spaces to control the number and positioning of stars.
- Call the functions with different values to display the required patterns.

Sample Values: 4 and 5

Sample Output:

Solid Square (n = 4)

```text
* * * *
* * * *
 * * * *
* * * *
```
Solid Triangle (n = 4)
```text
*
* *
* * *
* * * *
```
Equilateral Triangle (n = 5)
```text
    *
   ***
  *****
 *******
*********
```
Square Triangle (n = 5)
```text
**** ****
***   ***
**     **
*       *
```text

Square Diamond (n = 5)
```text
**** ****
***   ***
**     **
*       *
         
**     **
***   ***
**** ****
***** *****
```
Hollow Diamond Box (n = 5)
```text
**********
****  ****
***    ***
**      **
*        *
**      **
***    ***
****  ****
**********
```