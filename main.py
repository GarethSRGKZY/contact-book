from tkinter import *
from tkinter import messagebox

##WINDOW INIT
root = Tk()
root.geometry('700x550')
root.config(bg = '#40E9F7')
root.title("Contact Book")
root.resizable(0,0)
contactlist = [
    ['Abel','123049123'],
    ['Belle','234235432'],
    ['Caleb','345345345'],
]

Name = StringVar()
Number = StringVar()

##FRAME
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Calibri', 16), bg="#97F7DC", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
select.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

##FUNCTION FOR SELECT VALUE
def Selected():
    print("Hello",len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select A Name")
    else:
        return int(select.curselection()[0])