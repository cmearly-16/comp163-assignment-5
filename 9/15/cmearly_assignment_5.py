#Git Commit 1
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0
print("Sequence:", end=" ")
print(current_number, end=" ")
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    print(current_number, end=" ")
    step_count += 1
print()
print("Steps:", step_count)
print()

#Git Commit 2
print("=== Challenge 2: Prime Number Checker ===")
integer = int(input())
print(f"Enter a number: Testing divisors from 2 to {integer - 1}...")
prime = True
for i in range(2, integer):
    if integer % i == 0:
        prime = False
        break
if prime:
    print(f"{integer} is prime!")
else:
    print(f"{integer} is not prime (divisible by 3)")
print()

#Git Commit 3
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("    ", end="")
#AI used to find out how to use "col" and "row" to print the table properly.
for col in range(1, 11):
    print(f"{col:4}", end="")
print()
for row in range(1, 11):
    print(f"{row:2} ", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()

