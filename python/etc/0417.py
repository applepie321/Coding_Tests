result = []

for counter in range(5):
    a = input("Input number : ")
    if a not in result:
        result.append(a)

print(result)