Currency Symbol
In this exercise, you need to look for a currency symbol followed by digits and wrap them in ***.

input:

movie ticket: $15, popcorn: $8
movie ticket: €15, popcorn: €8
movie ticket: ₹15, popcorn: ₹8
output:

movie ticket: ***$15***, popcorn: ***$8***
movie ticket: ***€15***, popcorn: ***€8***
movie ticket: ***₹15***, popcorn: ***₹8***


HINT: Capture the currency symbol and digit in a named group. Use a replacement pattern to reformat the text.

Use the Learn Regex Tool for this exercise. For syntax help, refer to the Regex cheat sheet.

Find pattern: (?P < price >[$€₹]\d+)
Replacement Pattern: *** \g < price > ***