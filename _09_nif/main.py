codigos_control = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

dni_number = int(input("Numero DNI: "))
dni_completo = str(dni_number) + codigos_control[dni_number % 23]

print(dni_completo)
