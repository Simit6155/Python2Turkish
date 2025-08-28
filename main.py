translations = {
    "yazdir" : "print",
    "eger" : "if",
    "iken" : "while",
    "icin" : "for",
    "icinde" : "in",
    "tanim" : "def",
    "koy" : "input"
}

code = input("Kodunu buraya yaz, bitince entera bas: ")

for turkish, python in translations.items():
    code = code.replace(turkish, python)

exec(code)
