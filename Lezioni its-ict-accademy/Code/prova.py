def print_models(unprinted_designs: list[str], completed_models: list[str]) -> None:
    """Sposta i modelli non stampati alla lista dei modelli completati."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:", current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models: list[str]) -> None:
    """Mostra tutti i modelli stampati."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Liste iniziali
unprinted_designs: list[str] = ['phone case', 'robot pendant', 'Obs']
completed_models: list[str] = []  # Nome corretto

# Chiamata alle funzioni
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
