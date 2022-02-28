from tkinter import *
import webbrowser

def open_entry():
    webbrowser.open("sample.txt")

def read_entry():
    with open("sample.txt", "r") as f:
        print(f.read())

def log_entry():
    journal_entry = textbox.get()
    journal_entry = journal_entry + "\n"
    textbox.delete(0, END)
    with open("sample.txt", "a") as o:
        o.write(journal_entry)



def exit():
    root.destroy()

root = Tk()
root.geometry("500x400")
root.title("myJournal")

menubar = Menu(root)

filemenu1 = Menu(menubar, tearoff=0)


filemenu1.add_command(label="Past Entries", command=open_entry)
filemenu1.add_command(label="Quit", command=exit)


menubar.add_cascade(label="File", menu=filemenu1)
root.config(menu=menubar)

journal = Label(root, text="Log an Entry")
journal.pack()
textbox = Entry(root, bd=5, width=80)
textbox.pack()
save = Button(text="Save", command=log_entry)
save.pack()

root.mainloop()

