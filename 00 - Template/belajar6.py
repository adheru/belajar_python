# List
# List minuman dengan 2 dimensi
list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Kopi", "Es Campur", "Es Teler"]
]
print (list_minuman[1][1])

for menu in list_minuman:
    for minuman in menu:
        print (minuman)