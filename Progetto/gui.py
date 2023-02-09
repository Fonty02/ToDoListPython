import tkinter
from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
import os
if not os.path.exists("dafare.txt"):
    file = open("dafare.txt", "x")
    file.close()

def update(framePrincipale):
    if framePrincipale is not None:
        framePrincipale.destroy()
# CREAZIONE DEGLI STYLE
    stLb = ttk.Style()
    stLb.configure('m.TLabel', font=('Times', 15, 'bold', 'italic'))
    st = ttk.Style()
    st.configure('m.TButton', font=('Times', 15, 'bold', 'italic'))



# GESTIONE DEI FRAME
    framePrincipale=Frame(root,height=800, width=600)
    framePrincipale.pack(fill=BOTH)
    frame1 = Frame(framePrincipale, height=600, width=200)
    frame1.pack(fill=BOTH, side=LEFT)
    frame2 = Frame(framePrincipale, background="yellow", height=600, width=600)
    frame2.pack(fill=BOTH, expand=True)

# GESTIONE FRAME 1
    label = ttk.Label(frame1, text='LISTA DELLE TUE ATTIVITA', style='m.TLabel', background='grey', foreground='white')
    label.pack(fill=X)
    txtArea = scrolledtext.ScrolledText(frame1, height=100)
    def insertTask():
        f = open("dafare.txt", "r")
        cont = f.read()
        f.close()
        txtArea.insert(tkinter.INSERT, cont)
    insertTask()
    txtArea.configure(state="disabled")
    txtArea.pack(fill=BOTH)

# GESTIONE FRAME 2

    finestraCancellazione=None
    task_combobox=None
    def cancellazione():
        finestraCancellazione=Tk()
        finestraCancellazione.title("Cancella una nuova attività")
        finestraCancellazione.geometry("600x400")
        finestraCancellazione.resizable(FALSE, FALSE)
        finestraCancellazione.iconbitmap('./icona.ico')
        task_combobox=ttk.Combobox(finestraCancellazione,width=100)
        task_combobox['state']='readonly'
        f = open("dafare.txt", "r")
        cont=list()
        for stringa in f:
            cont.append(stringa)
        f.close()
        task_combobox['values']=[cont[i] for i in range(0,len(cont))]
        task_combobox.pack(fill=X)
        task_combobox.current(0)
        def canc():
            scelta=task_combobox.get()
            cont.remove(scelta)
            file = open("dafare.txt", "w")
            for task in cont:
                file.write(task)
            file.close()
            finestraCancellazione.destroy()
            update(framePrincipale)

        buttonCanc = ttk.Button(finestraCancellazione, text='Conferma', command=canc)
        buttonCanc.pack()
        finestraCancellazione.mainloop()
    button1 = ttk.Button(frame2, text='Cancella', style='m.TButton', command=cancellazione)

    finestraModifica = None
    def modifica():
        finestraModifica=Tk()
        finestraModifica.title("Modifica un'attività")
        finestraModifica.geometry("600x400")
        finestraModifica.resizable(False,False)
        finestraModifica.iconbitmap('./icona.ico')
        labelScelta=Label(finestraModifica, text='Scegli quale attività modificare',pady=15)
        labelScelta.pack(fill=X)
        task_combobox=ttk.Combobox(finestraModifica,width=100)
        task_combobox['state']='readonly'
        f = open("dafare.txt", "r")
        cont = list()
        for stringa in f:
            cont.append(stringa)
        f.close()
        task_combobox['values'] = [cont[i] for i in range(0, len(cont))]
        task_combobox.pack(fill=X)
        task_combobox.current(0)
        labelNuova = Label(finestraModifica, text='Inserisci la nuova attivitò',pady=15,width=300)
        labelNuova.pack(fill=X)
        nuovaTask_entry = ttk.Entry(finestraModifica)
        nuovaTask_entry.pack()
        def conf() :
            scelta = task_combobox.get()
            i=cont.index(scelta)
            nuova=nuovaTask_entry.get()
            cont.insert(i,nuova+'\n')
            cont.remove(scelta)
            if len(nuova)==0 :
                messagebox.showerror(title='Attenzione',message="Inserire qualcosa o uscire")
                finestraModifica.destroy()
                modifica()
            else :
                file = open("dafare.txt", "w")
                for task in cont:
                    file.write(task)
                file.close()
                finestraModifica.destroy()
                update(framePrincipale)
        buttonIns = ttk.Button(finestraModifica, text='Conferma', command=conf)
        buttonIns.pack()
        finestraModifica.mainloop()

    button2 = ttk.Button(frame2, text='Modifica', style='m.TButton',command=modifica)





    # Dichiarazione Tools dell'inserimento
    finestraInserimento = None
    nuovaTask_entry = None

    # inserimento di una nuova task
    def inserimento():
        finestraInserimento = Tk()
        finestraInserimento.title("Inserisci una nuova attività")
        finestraInserimento.geometry("600x400")
        finestraInserimento.resizable(False, False)
        finestraInserimento.iconbitmap('./icona.ico')
        nuovaTask_entry = ttk.Entry(finestraInserimento)
        nuovaTask_entry.pack()
        nuovaTask_entry.focus()

        def add():
            if len(nuovaTask_entry.get())==0 :
                messagebox.showerror(title='Attenzione',message="Inserire qualcosa o uscire")
                finestraInserimento.destroy()
                inserimento()
            else:
                file = open("dafare.txt", "a")
                file.write(nuovaTask_entry.get() + '\n')
                file.close()
                finestraInserimento.destroy()
                update(framePrincipale)

        buttonIns = ttk.Button(finestraInserimento, text='Conferma', command=add)
        buttonIns.pack()
        finestraInserimento.mainloop()
    button3 = ttk.Button(frame2, text='Inserisci', style='m.TButton', command=inserimento)



    button1.pack(pady=75)
    button2.pack(pady=75)
    button3.pack(pady=75)
    contenuto=txtArea.get("1.0",END)
    if len(contenuto)==1:
        button1['state']='disabled'
        button2['state'] = 'disabled'

# ROOT
root =Tk()
root.title("TODO LIST")  # dai titolo
root.geometry("800x600")
root.resizable(FALSE, FALSE)
root.iconbitmap('./icona.ico')
framePrincipale=None
update(framePrincipale)  # avvia schermata principale
root.mainloop()