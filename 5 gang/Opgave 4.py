"""Opgave 4 - vilkårligt antal parametre.

Lav en funktion “borrow_books” som kan tage et vilkårligt antal strings som input - altså titler på bøger.
Funktionen skal så skrive ud hvor mange bøger der bliver angivet som parametre
(husk at parametrene i dette tilfælde kommer ind i funktionen som en liste)

samt alle titlerne (med en for loop)
Test din funktion med f.eks. borrow_books(“Idioten”) og
borrow_books(“Kældermennesket”, “Forbrydelse og Straf”) eller find på dine egne titler!

I det første tilfælde skal funktionen udskrive:
antal bøger : 1
Idioten

I det andet tilfælde skal funktionen udskrive:
antal bøger : 2
Kældermennesket
Forbrydelse og Straf.
"""

def borrow_books(*books):
    """funktion der tager mod vilkårligt antal strings (Bogtitler) og udskriver antallet af bøger samt titlerne."""
    print("antal bøger:" + str(len(books)))
    for book in books:
        print(book)

borrow_books("Idioten")

print("")

borrow_books("Kældermennesket", "Forbrydelse og Straf")