try:
    a = int(input())
    b = int(input())

    if b == 0:
        raise Exception("NE STAA 0")
    print(c)
    c = a/b

except Exception as e:
    print(e)
else:
    print("IF ELSE BSLOCK")
finally:
    print("ALWAYS get printed")


