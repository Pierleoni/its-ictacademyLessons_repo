from typing import Any

# # #Inizio con una lista di 3 elementi e una lista vuota a cui dovrò aggiungere questi elementi 
# # unprinted_designs:list[str] = ['phone case', 'robot pendant', 'Obs']
# # completed_models:list[str]= []

# # #Uso ciclo while perché devo eliminare gli elementi dalla prima lista e appenderli nella seconda lista
# # while unprinted_designs:
# #     #Uso la funzione .pop() perché mi cancella gli elementi di una lista ad uno specifico index
# #     #Di default, se la funzione non ha l'argomento, che va ad indicare l'indice dell'elemento da rimuovere, elemina solo l'ultimo elemento che si trova all'ultimo indice della lista
# #     #Salvo unprinted_designs in una variabile che punta agli indici delgi elementi che la funzione pop() sta eliminando
# #     current_designs = unprinted_designs.pop()
# #     print(f"Printing Model:{current_designs}")
# #     #Appendo gli elementi della lista current_designs alla lista vuota (completed_models)
# #     completed_models.append(current_designs)

# # #Visualizzo tutti gli elementi di completed_models
# # print("\nThe following models have been print:")
# # #Utilizzo il ciclo for per stampare ogni elemento di completed_models correttamente
# # for completed_model in completed_models:
# #     print(completed_model)

# def print_models(unprinted_designs: list[str], completed_models: list[str]) -> None:
#     """Sposta i modelli non stampati alla lista dei modelli completati."""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model:", current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models: list[str]) -> None:
#     """Mostra tutti i modelli stampati."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# # Liste iniziali
# unprinted_designs: list[str] = ['phone case', 'robot pendant', 'Obs']
# completed_models: list[str] = []  # Nome corretto

# # Chiamata alle funzioni
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def describe_person(name:str, age:int, city:str) ->Any:
#     greetings = f"Hello my name is {name}, I'm {age} years old and I live in {city}"
#     return greetings


# print(describe_person(age=25, city="Rome", name="Carlo"))

def add(*args):
    return args  # Restituisce tutti gli argomenti come una tupla

print(add(2, 3))  # Output: (2, 3)

valori = [1, 2, 4, 5, 10, 56, "Hello"]
print(add(*valori))  # Output: (1, 2, 4, 5, 10, 56, 'Hello')


# def stampa(*args):
#     print(args)

myList = [1,2,3,4,5,6,7,8,9]

print(*myList)


def alpha():
    print("Alpha")

