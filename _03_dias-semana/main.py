dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

dia_buscar = input("Dia para buscar: ")

try:
    result = dias.index(dia_buscar.lower())
    print("Found at position", result)
except ValueError:
    print("Not found")
