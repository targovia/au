

a = "mika"
b = "mika1"
print(a != b)

h = "milenski    pipilota"
print(len(h))

'   spacious   '.lstrip()

print('www.example.com'.lstrip('cmowz.'))

x = "Milen Georgiev, Milen Georgiev Milen Georgiev Milen Georgievn"
print(x.split(" ", maxsplit=3))
y = "Kartagenosviasta"

print(x[::-1])
print(x[0:x.index(",")])

t = "String for rormating"
r = "novia string"
print("Novia string %s nad %s" %(t, r))

print(f'kor za levski{t} nad {r}')

pa = "marmalad"
ra = 12345
print(f"Kur za levski{ra}{pa}")

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword