fw = open("demofile.txt", "w")
fw.write("fist line")
fw.close()


with open("papas.txt", "a") as fr:
    fr.write("novia naching")