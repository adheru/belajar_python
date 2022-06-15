# Dictionary
mynameis = {
    "Name": "Ade Heru Prasetiyo",
    "Umur": 22,
    "Hobby": ["coding", "membaca", "cocok tanam"],
    "menikah": False,
    "Sosial_Media": {
        "Instagram": "@adeheru_p",
        "Twitter": "@aheru_p"
    } 
}

print("Len is : %s" % len(mynameis))
print("My name is %s" % mynameis["Name"])
print("Twitter: %s" % mynameis["Sosial_Media"]["Twitter"])
print("Instagram: %s" % mynameis["Sosial_Media"]["Instagram"])