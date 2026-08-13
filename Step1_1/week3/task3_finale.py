n = int(input("Enter a number: "))
if n <= 0:
    print("Invalid input")
else:
    for i in range(n + 1):
        if i % 2 == 0:
            continue
        print(i)


while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    if n == 5:
        pass
    print(n)
print("Finished")

for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()