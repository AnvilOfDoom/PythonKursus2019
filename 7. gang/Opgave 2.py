import tkinter as tk

root = tk.Tk() #denne skal defineres i følge https://www.python-course.eu/tkinter_labels.php og definerer vist vinduet

#tilføjer frame
frame = tk.Frame(root)
frame.pack()

#besked der skal stå i vinduet til at starte med
besked = "Hej, velkommen til mit program\n\n\n"

w = tk.Label(frame, text=besked)    #laver et vindue med teksten i besked
w.pack() #dette gør vinduet tilpasses indholdet

#quit-button
quit_button = tk.Button(frame, text="QUIT", fg="red", command=quit)
quit_button.pack()

#Change text button
def change():
    w.config(text="Du har trykket på knappen!\n")

change_text_button = tk.Button(frame, text="Change text", command=change)   #bemærk ingen () efter funktionskald, hvis de er der så kaldes funktionen når programmet starter
change_text_button.pack()

#Text-felt tilføjes
text_field = tk.Text(frame, height=4, width=50)
text_field.pack(side=tk.LEFT, fill=tk.Y)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
text_field.insert(tk.END, quote)

#scroll bar
s = tk.Scrollbar(frame)
s.pack(side=tk.RIGHT, fill=tk.Y)

s.config(command=text_field.yview) #hvis der sættes () efter yview så virker musehjul, men ikke knapper på scrollbar
text_field.config(yscrollcommand=s.set)


root.mainloop() #dette får programmet til at køre til man lukker vinduet