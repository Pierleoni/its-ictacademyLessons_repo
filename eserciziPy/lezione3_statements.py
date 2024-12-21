numbers:list=[]
lunghezza=int(input("inserisci num quanto vuoi che sia lunga la lista:"))

for num in range(1, lunghezza +1): 
    numbers.append(num)
    print(numbers)


number:list=[]
#casting: cosa è? Serve per convertire la stringa in un integer per questo su questa riga lenght o lunghezza \
    #devo assegnrargli il valore int a fin che mi converta questo valore str in integer
lenght=int(input("inserire il valore:"))
for numb in range(2, lenght +2):
    number.append(numb)
    print(number)
