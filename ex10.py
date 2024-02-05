blocks = int(input("Dime el número de bloques: "))
height = 0
total_blocks = 0

while total_blocks < blocks:
    height += 1
    total_blocks += height

print("La altura de la pirámide es:", height)
