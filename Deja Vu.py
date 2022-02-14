String = input()

alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets = list(alphabets)

Unique = False
DejaVu = False

for l in alphabets:
    if String.count(l) > 1:
        DejaVu = True

    else:
        Unique = True

if DejaVu:
    print('Deja Vu')

elif Unique:
    print('Unique')
