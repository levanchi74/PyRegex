Exercise - List all cars not made by Honda
Use the Learn Regex Tool for this exercise. For syntax help, refer to the Regex cheat sheet.

Write a pattern to match all non-Honda cars (case insensitive)

Input:
Honda Civic
Honda Accord
Honda Insight
Hyundai Accent
Toyota Corolla
Toyota Camry
Toyota Prius
Tesla Model 3
Tesla Model S
Tesla Model X
Expected Output:
Hyundai Accent
Toyota Corolla
Toyota Camry
Toyota Prius
Tesla Model 3
Tesla Model S
Tesla Model X

Answer: (?im) ^ (?!honda). +

This pattern uses a negative look ahead to exclude honda