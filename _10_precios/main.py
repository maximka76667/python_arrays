import sys
precios = []

mayor_precio = 0
menor_precio = sys.float_info.max  # Numero float maximo posible
suma_precios = 0
precios_debajo_30 = 0

for i in range(0, 10, 1):
    precio = float(input("Nuevo precio: "))
    precios.append(precio)
    suma_precios += precio
    
    if precio < 30:
        precios_debajo_30 += 1
        
    if precio > mayor_precio:
        mayor_precio = precio
        
    if precio < menor_precio:
        menor_precio = precio
    
print("Mayor:", mayor_precio)
print("Menor:", menor_precio)
print("Medio:", suma_precios / 10)
print("Debajo 30:", precios_debajo_30)
