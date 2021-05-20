linha = int(input())
coluna = int(input())
if (linha%2 == 0):
    if (coluna%2 == 0):
        print("1")
    else:
        print("0")
else:
    if (coluna%2 == 0):
        print("0")
    else:
        print("1")