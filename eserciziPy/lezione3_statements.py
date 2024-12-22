numbers:list=[]
lunghezza=int(input("inserisci num quanto vuoi che sia lunga la lista:"))

for num in range(1, lunghezza +1): 
    numbers.append(num)
    print(numbers)


number:list=[]
#casting: cosa è? Serve per convertire la stringa in un integer per questo su questa riga lenght o lunghezza \
    #devo assegnrargli il valore int a fin che mi converta questo valore str in integer
# lenght=int(input("inserire il valore:"))
# for numb in range(2, lenght +2):
#     number.append(numb)
#     print(number)


# lista_1 = [1, 2, 3]
# lista_2 = ["a", "b", "c"]

# for lettera in lista_2:
#     for numero in lista_1:
#         print(lettera, numero)


lista_1 = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_2 = ["a", "b", "c"]
lista_1 in range (10)
print(lista_1)
for lettera in lista_2:
    for numero in lista_1:
        print(lettera, numero)
        


L = [[("a", 1), ("a", 2), ("a", 3)],
    [("b", 1), ("b", 2), ("b", 3)],
    [("c", 1), ("c", 2), ("c", 3)]]

print(L[1][1])