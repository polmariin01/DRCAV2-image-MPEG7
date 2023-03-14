import os


print(os.getcwd())

directori = "db/UKentuckyDatabase/"

llista = os.listdir(directori)

arxiu = open("db/UKentuckyDatabase/llista.txt", "w")

for dir in llista:
    arxiu.write(directori + dir + "\n")