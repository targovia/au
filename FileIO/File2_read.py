f = open("pap2.txt", "r") # a - append, w - wried
data = f.readline()
f.close()
print(data)

f = open("pap2.txt", "r+")
f.write("NOVIO RED")
f.close()

babangida = open("paps.txt", "w")
babangida.write("kos")
babangida.close()

with open('pap2.txt', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
print(read_data)

import json
x = [1, 'simple', 'list']
print(type(x))
new = json.dumps(x)
print(type(new))