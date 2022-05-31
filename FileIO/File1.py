
# f = open("C:\\Users\\mgeorgiev29\\PycharmProjects\\au\\FileIO\\pap.txt", "w")
# f.write("this is first line")
# f.close()

f = open("C:\\Users\\mgeorgiev29\\PycharmProjects\\au\\FileIO\\pap2.txt", "a")

list= [1, 2, 3, 4, 5, 6]
for items in list:
    f.write(str(items) + "\n")

f.close()


f = open("pasok.csv", "a")
f.write("123456")
f.close()
