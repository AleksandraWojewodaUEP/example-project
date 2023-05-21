def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod

def kwadrat():
    return 0, 0

def trapez():
    return 0, 0

print(f'Pole i obwod wynosza: {trojkat(10, 15, 12, 8)}')
print()
