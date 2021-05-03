Filter by price
Write a pattern to match items whose price do not end with .99

Sample Input:
chair 4.98
coffee 1.99
fan 10.97
car 11499.59
banana 0.09
Expected Output:
chair 4.98
fan 10.97
car 11499.59
banana 0.0

(?m).+(?<!\.99)$

We use a negative look behind to exclude products that end in .99