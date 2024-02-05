frase = input("Dime una frase: ")
letra = input("Dime una letra: ")

conteo = frase.upper().count(letra.upper())
print(f"La letra '{letra}' aparece {conteo} veces en tu frase.")
