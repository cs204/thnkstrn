camel = input("Верблюжий стиль: ")
snake = ""
for char in camel:

    if char.isupper():
        snake += '_' + char.lower()
    else:
        snake += char

print(snake)