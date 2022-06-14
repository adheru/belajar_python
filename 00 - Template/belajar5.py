# Loopingnilai
num1 = 'y'
num2 = 0

while(True):
    num2 += 1
    num1 = input("Loop y/n? ")
    if num1 == 'n':
        break

print(f"Total looping: {num2}")