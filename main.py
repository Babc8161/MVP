from tkinter import *
import webbrowser

def read_entry():
    """Opens the text written by user"""
    webbrowser.open("myJournal.txt")


def log_entry():
    journal_entry = textbox.get()
    journal_entry = journal_entry + "\n"
    textbox.delete(0, END)
    with open("myJournal.txt", "a") as o:
        o.write(journal_entry)

def exit():
    root.destroy()

root = Tk()
root.geometry("500x400")
root.title("myJournal")

menubar = Menu(root)

options = Menu(menubar, tearoff=0)

options.add_command(label="Past Entries", command=read_entry)
options.add_command(label="Exit", command=exit)

menubar.add_cascade(label="Options", menu=options)
root.config(menu=menubar)

journal = Label(root, text="Log an Entry")
journal.pack()
textbox = Entry(root, bd=5, width=80)
textbox.pack()
save = Button(text="Save", command=log_entry)
save.pack()

root.mainloop()

