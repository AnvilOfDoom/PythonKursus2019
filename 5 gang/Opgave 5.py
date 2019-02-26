"""Opgave 5 - brug af et modul
Du skal lave et nyt model (dvs. en ny python fil) - kald den f.eks. “books.py”
Flyt funktionen borrow_books fra opgave 4 over i denne fil.

I en anden python fil - (kald den f.eks. opgave5.py) skal du så importere books ved at skrive : import books as b

Du kan ny kalde funktionen fra dit “books.py” modul ved at skrive
b.borrow_books(“bog navn”)

Prøv det og få det til at virke - ellers se til sidst i denne opgave, hvis det ikke virker.

Derefter så prøv at kopiere din funktion fra opgave 2 over i dette modul også og prøv at importere dette modul
også i din “opgave5.py”, således at du nu også kan kalde denne funktion fra din “opgave5.py” fil.

Hvis du får en warning/fejl i din “opgave5.py” fil ved din “import…..”
så prøv at følge svaret fra stackoverflow på dette link :
https://stackoverflow.com/questions/28705029/pycharm-error-no-module-when-trying-to-import-own-module-python-script"""

import books as b

b.borrow_books("Hobbitten")


talliste = [1, 2, 3]

print(b.sum_liste_ii(talliste))


