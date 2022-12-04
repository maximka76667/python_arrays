numbers = []

for i in range(0, 10, 1):
    new_number = int(input("Nuevo numero: "))
    numbers.append(new_number)
    
    
search_number = int(input("Numero para buscar: "))
print(numbers.count(search_number))
