
while True:
    letra= input ("Digite uma letra: ").lower()
    match letra:
    case "a"| "e"| "i"| "o"| "u":
        print("É uma vogal")
    case _:
        print("É uma consoante")
