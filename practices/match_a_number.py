Match a number
1. Write a pattern to match one or more digits. In the below text, the pattern should match 1, 123, 12345. However, it should not match ABCD123

Answer: \b\d+\b

2. Extend the previous pattern to now match an optional decimal point and two digits. For example, the pattern should match 1234.56 and 57890 but not match 1234A56

Answer: \b\d+(\.\d{2})?\b

3. Extend the pattern from the previous question to now match an optional comma followed by three digits. This optional comma and the 3-digit group can appear as many times as possible.

Answer: \b\d+(,\d{3})*(\.\d{2})?\b