import os


print(os.getcwd())

directori = "./db/UKentuckyDatabase/"

llista = os.listdir(directori)

arxiu = open("db/UKentuckyDatabase/UKentuckyDatabaseLlista.txt", "w")

for dir in llista:
    #print(dir)
    arxiu.write(directori + dir + "\n")