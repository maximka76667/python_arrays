numbers = []

for i in range(0, 10, 1):
    new_number = int(input("Nuevo numero: "))
    numbers.append(new_number)
    
numbers.reverse()
print(numbers)