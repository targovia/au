
f = open("C:\\Users\\mgeorgiev29\\PycharmProjects\\au\\FileIO\\123.txt", "w")
l = [1, 3, 333, 423]
for i in l:
    f.write(str(i) + "\n")
f.close()