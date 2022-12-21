from biudzetas import Biudzetas
from tkinter import Tk, Label, Entry, Button, Listbox, Frame

biudzetas = Biudzetas()

langas = Tk()
pajamos1 = Frame(langas)
islaidos2 = Frame(langas)
viskas3 = Frame(langas)

def ui_ivesti_pajamas():
    biudzetas.prideti_pajamu_irasa(suma1.get(), siuntejas1.get(), info1.get())
    suma1.delete(0, 'end')
    siuntejas1.delete(0, 'end')
    info1.delete(0, 'end')
    suma1.focus()

uzrasas1 = Label(pajamos1, text="Įveskite pajamas:")
suma_uzrasas1 = Label(pajamos1, text="Suma")
suma1 = Entry(pajamos1)
siuntejas_uzrasas1 = Label(pajamos1, text="Siuntėjas")
siuntejas1 = Entry(pajamos1)
info_uzrasas1 = Label(pajamos1, text="Informacija")
info1 = Entry(pajamos1)
pajamos_button1 = Button(pajamos1, text="Įvesti", command=ui_ivesti_pajamas)

pajamos1.pack()
islaidos2.pack()
viskas3.pack()

uzrasas1.pack()
suma_uzrasas1.pack()
suma1.pack()
siuntejas_uzrasas1.pack()
siuntejas1.pack()
info_uzrasas1.pack()
info1.pack()
pajamos_button1.pack()

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
