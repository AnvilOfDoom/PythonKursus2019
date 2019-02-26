def borrow_books(*books):
    """funktion der tager mod vilkårligt antal strings (Bogtitler) og udskriver antallet af bøger samt titlerne."""
    print("antal bøger:" + str(len(books)))
    for book in books:
        print(book)

def sum_liste_ii(liste):
    """Lægger tallene i input-listen sammen og returnerer summen"""
    output_liste = 0
    for tal in liste:
        output_liste += tal
    return output_liste