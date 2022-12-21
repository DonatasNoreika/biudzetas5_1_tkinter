from biudzetas import Biudzetas
from tkinter import Tk, Label, Entry, Button, Listbox, Frame, END

biudzetas = Biudzetas()

langas = Tk()
pajamos1 = Frame(langas)
islaidos2 = Frame(langas)
viskas3 = Frame(langas)

def ui_ivesti_pajamas():
    biudzetas.prideti_pajamu_irasa(float(suma1.get()), siuntejas1.get(), info1.get())
    suma1.delete(0, END)
    siuntejas1.delete(0, END)
    info1.delete(0, END)
    suma1.focus()

def ui_ivesti_islaidas():
    biudzetas.prideti_islaidu_irasa(float(suma2.get()), atsiskaitymo_budas2.get(), isigyta_preke_paslauga2.get(), info2.get())
    suma2.delete(0, END)
    atsiskaitymo_budas2.delete(0, END)
    isigyta_preke_paslauga2.delete(0, END)
    info2.delete(0, END)
    suma2.focus()

def ui_istrinti():
    biudzetas.istrint_irasa(blokas.curselection()[0])
    blokas.delete(0, END)
    blokas.insert(END, *biudzetas.zurnalas)


# Pajamų formos grafiniai objektai:
uzrasas1 = Label(pajamos1, text="Įveskite pajamas:")
suma_uzrasas1 = Label(pajamos1, text="Suma")
suma1 = Entry(pajamos1)
siuntejas_uzrasas1 = Label(pajamos1, text="Siuntėjas")
siuntejas1 = Entry(pajamos1)
info_uzrasas1 = Label(pajamos1, text="Informacija")
info1 = Entry(pajamos1)
pajamos_button1 = Button(pajamos1, text="Įvesti", command=ui_ivesti_pajamas)

# Išlaidų formos grafiniai objektai:
uzrasas2 = Label(pajamos1, text="Įveskite išlaidas:")
suma_uzrasas2 = Label(pajamos1, text="Suma")
suma2 = Entry(pajamos1)
atsiskaitymo_budas_uzrasas2 = Label(pajamos1, text="Atsiskaitymo budas")
atsiskaitymo_budas2 = Entry(pajamos1)
isigyta_preke_paslauga_uzrasas2 = Label(pajamos1, text="Įsigyta prekė ar paslauga")
isigyta_preke_paslauga2 = Entry(pajamos1)
info_uzrasas2 = Label(pajamos1, text="Informacija")
info2 = Entry(pajamos1)
islaidos_button2 = Button(pajamos1, text="Įvesti", command=ui_ivesti_islaidas)

# Pajamų ir įrašų atvaizdavimas
blokas = Listbox(viskas3)
blokas.insert(END, *biudzetas.zurnalas)
istrinti_button = Button(viskas3, text="Ištrinti įrašą", command=ui_istrinti)
# balansas = Label(viskas3, text=str(biudzetas.gauti_balansa()))

pajamos1.pack()
islaidos2.pack()
viskas3.pack()

# Pajamų objektų pakavimas:
uzrasas1.pack()
suma_uzrasas1.pack()
suma1.pack()
siuntejas_uzrasas1.pack()
siuntejas1.pack()
info_uzrasas1.pack()
info1.pack()
pajamos_button1.pack()

# Išlaidų objektų pakavimas:
uzrasas2.pack()
suma_uzrasas2.pack()
suma2.pack()
atsiskaitymo_budas_uzrasas2.pack()
atsiskaitymo_budas2.pack()
isigyta_preke_paslauga_uzrasas2.pack()
isigyta_preke_paslauga2.pack()
info_uzrasas2.pack()
info2.pack()
islaidos_button2.pack()

# Visų kitų objektų pakavimas:
blokas.pack()
# balansas.pack()
istrinti_button.pack()

langas.mainloop()


# while True:
#     ivedimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - ataskaita\n4 - balansas\n0 - išeiti\n"))
#     if ivedimas == 1:
#         suma = float(input("Įveskite sumą: "))
#         siuntejas = input("Įveskite siuntėją: ")
#         info = input("Įveskite papildomą informaciją: ")
#         biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
#     if ivedimas == 2:
#         suma = float(input("Įveskite sumą: "))
#         atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
#         isigyta_preke_paslauga = input("Įsigyta prekė ar paslauga: ")
#         info = input("Įveskite papildomą informaciją: ")
#         biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
#     if ivedimas == 3:
#         biudzetas.gauti_ataskaita()
#     if ivedimas == 4:
#         print("Balansas:", biudzetas.gauti_balansa())
#     if ivedimas == 0:
#         print("Viso gero")
#         break
