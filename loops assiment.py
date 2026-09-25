print("Countdown Timer:")
for c in range(10, 0, -1):
    print(f"Countdown: {c}")
print("Happy New Year!")
answer = "y" 

while answer == "y":
    print("Countdown Timer:")
    for c in range(10, 0, -1):
        print(f"Countdown: {c}")
    print("Happy New Year!")

    print("Odd numbers up to 100:")
    for number in range(1, 101):
        if number % 2 != 0:
            print(number, end=" ")
    print()

    print("Even numbers up to 100:")
    number = 2
    while number <= 100:
        print(number, end=" ")
        number += 2
    print()

    answer = input("Do you want to see the loops again? (y/n): ").strip().lower()