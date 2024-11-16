from tkinter import *
from tkinter import ttk
import doctorDataAcess
import tkinter.messagebox
import doctorDatabase
from tkinter import messagebox
import patientdatabase


# font
submitbtn_font = ("Comic Sans MS", 14)
question_font = ("Microsoft Sans Serif", 14)
intro_font=("Microsoft Sans Serif", 14)

# color
background_color="#CDCDC1"
submitbtn_color = "#9575cd"
entry_color="#ede7f6"
btn_color = "#8B8B83"



# functions
def doctor1():
    username=user_doc.get()
    password=pass_doc.get()
    code=id_doc.get()
    doctor=doctorDatabase.fetch_doctors()

    if not (username and password and code):
            messagebox.showerror('Error','Enter all fields')
    else:
        code=int(id_doc.get())
        for i in range (len(doctor)):
            if doctor[i][0]==code and doctor[i][1]==username and doctor[i][2]==password:
                window.destroy()
                doctorDataAcess.dc()
           

# main window
window = Tk()
window.title("Login")
window.geometry("500x300")
window.config(bg=background_color)
window.resizable(False,False)

# display
doct = LabelFrame(window, text='Login',background=background_color,
              font=('Comic Sans MS', 36))

id_docEntry = Label(doct, text="Enter your code",background=background_color,font=question_font)
id_doc= Entry(doct, width=22,background=entry_color)
user_docEntry = Label(doct, text="Enter your username",background=background_color,font=question_font)
user_doc= Entry(doct, width=22,background=entry_color)
pass_docEntry = Label(doct, text="Enter your password",background=background_color,font=question_font)
pass_doc= Entry(doct, width=22,background=entry_color)
btn_doctor = Button(window, text='CHECK', background=btn_color,font=submitbtn_font,
                        cursor='hand2',border=3, height=2, width=12, command=doctor1)

# packing
doct.pack()
id_docEntry.pack()
id_doc.pack()
user_docEntry.pack()
user_doc.pack()
pass_docEntry.pack()
pass_doc.pack()
btn_doctor.pack()

# placing
btn_doctor.place(x="170",y="230")

window.mainloop()


