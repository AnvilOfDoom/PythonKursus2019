import tkinter as tk

root = tk.Tk() #denne skal defineres i følge https://www.python-course.eu/tkinter_labels.php og definerer vist vinduet

besked = "Hej, velkommen til mit program\n\n\n"

w = tk.Label(root, text=besked)
w.pack() #dette gør vinduet tilpasses indholdet

root.mainloop() #dette får programmet til at køre til man lukker vinduet





