salaries = []

for i in range(0, 12, 1):
    new_number = int(input("Nuevo numero: "))
    salaries.append(new_number)
    
increasedSalaries = 0    
    
def increaseSalary(salary): 
    # Asignar que variable increasedSalaries 
    # ya fue creada fuera de funcion
    global increasedSalaries
    
    if salary < 800:
        increasedSalaries += 1
        return salary + 100
    
    return salary

salaries = list(map(increaseSalary, salaries))    

print(salaries)
print("Cantidad de sueldos actualizados:", increasedSalaries)