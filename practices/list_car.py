Exercise - List cars that meet specified criteria
List all the cars that do not start with exl or xle

Input:
exl-accord
ex-accord
se-camry
xle-camry
exl-civic
Expected Output:
ex-accord
se-camry


(?m)^(?!(exl|xle)).+$

used negative look ahead with multiple pre-condition.