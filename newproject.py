from tkinter import *
import requests
import tkinter.messagebox


root = Tk()
root.title("myJournal")
root.geometry("500x400+200+300")

# Popup with new feature info
tkinter.messagebox.showinfo("New Feature!", "You can now add real time bitcoin prices to your journal entries!")



def savefile():
    """Saves the current entry to the journal."""

    with open("myJournal.txt", "w") as o:
        if o is None:
            return
        text = str(entry.get(1.0, END))
        o.write(text)

def erase():
    """Erases whatever is in the textbox. Asks the user if they really want to erase it."""

    answer = tkinter.messagebox.askquestion("Erase", "Do you really want to erase entry? This cannot be undone.")
    if answer:
        entry.delete(1.0, END)


def read_entries():
    """Opens up the journal so the user can read their entries."""

    with open("myJournal.txt", "r") as f:
        if f is not None:
            content = f.read()
    entry.insert(INSERT, content)


# Retrieve info about current bitcoin prices
def binance():
    with open("myJournal.txt", "w+") as o:
        url = 'https://thawing-mountain-55789.herokuapp.com/api/binance/realtime'
        r = requests.get(url, params={"bid": "ask"})
        o.write(str(r.text) + "\n" + "\n")

def coinbase():
    with open("myJournal.txt", "w+") as o:
        url = 'https://thawing-mountain-55789.herokuapp.com/api/coinbase/realtime'
        r = requests.get(url, params={"bid": "ask"})
        o.write(str(r.text) + "\n" + "\n")

def kraken():
    with open("myJournal.txt", "w+") as o:
        url = 'https://thawing-mountain-55789.herokuapp.com/api/kraken/realtime'
        r = requests.get(url, params={"bid": "ask"})
        o.write(str(r.text) + "\n" + "\n")


# Buttons and their placements on the app
bsavefile = Button(root, text="Save", command=savefile)
bsavefile.place(x=450, y=10)

berase = Button(root, text="Erase", command=erase)
berase.place(x=410, y=10)

bopenfile = Button(root, text="Read Entries", command=read_entries)
bopenfile.place(x=10, y=10)

bbinance = Button(root, text="Get Binance", command=binance)
bbinance.place(x=130, y=10)

bcoinbase = Button(root, text="Get Coinbase", command=coinbase)
bcoinbase.place(x=210, y=10)

bkraken = Button(root, text="Get Kraken", command=kraken)
bkraken.place(x=295, y=10)


# The text box to write in
entry = Text(root, height=60, width=60, wrap=WORD)
entry.place(x=10, y=50)


root.mainloop()
