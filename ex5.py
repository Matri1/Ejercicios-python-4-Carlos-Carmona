capitalinicial = float(input("Cantidad a invertir?: "))
tasainteresanual = float(input("Interés anual?: "))
numaños = int(input("Ingresa el número de años: "))

for i in range(1, numaños + 1):
    capitalinicial *= (1 + tasainteresanual / 100)
    print(f"Año {i}: {round(capitalinicial, 2)}")
