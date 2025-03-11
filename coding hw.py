def find(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter Largest number: "))
num2 = int(input("Enter Smallest number: "))

lcm = find(num1, num2)

print("LCM is:", lcm)