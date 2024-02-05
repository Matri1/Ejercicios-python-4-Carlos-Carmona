userword = input("Di una palabra: ")
userword = userword.upper()

for letter in userword:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    print(letter)
