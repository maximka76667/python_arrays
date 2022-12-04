n = int(input("Numero alumnos: "))

# Nota solo puede estar entre 0 y 10
nota_maxima = 0
nota_minima = 10

# Array de notas
notas = []

# Suma para calcular nota media
suma_notas = 0

for i in range(0, n, 1):
    nota = int(input("Nota: "))
    
    if nota < nota_minima:
        nota_minima = nota
        
    if nota > nota_maxima:
        nota_maxima = nota

    suma_notas += nota        
    notas.append(nota)

print("Todas las notas:", notas)    
print("Nota maxima:", nota_maxima)
print("Nota minima:", nota_minima)
print("Nota media del curso:", suma_notas / n)