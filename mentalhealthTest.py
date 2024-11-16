from tkinter import *
from tkinter import ttk
import bipolartest
import depressiontest
import ADHDtest
import psychosistest
import anxietytest
import PTSDtest
import tkinter.messagebox
from PIL import Image,ImageTk
import patientdatabase
import doctorDatabase

# color

nextbtn_color = "#9fa8da"
submitbtn_color = "#a5d6a7"

# font

nextbtn_font = ("Haettenschweiler", 14)
btn_font=('Comic Sans MS', 10)
submitbtn_font = ("Rockwell Extra Bold", 14)
intro_font=('Comic Sans MS', 36)
question_font = ("Times New Roman (Headings CS)", 16)


write = dict()


# bipolar

def bipolar():
    window.destroy()
    bipolartest.bipolar()


# depression

def depression():
    window.destroy()
    depressiontest.depression()


# ADHD

def ADHD():
    window.destroy()
    ADHDtest.ADHD()

# psychosis

def psychosis():
    window.destroy()
    psychosistest.psychosis()


# PTSDs

def PTSD():
    response = tkinter.messagebox.askquestion(
        "question", """Sometimes things happen to people that are unusually or 
        especially frightening, - horrible, or traumatic. For example:
            - a serious accident or fire
            - a physical or sexual assault or abuse
            - an earthquake or flood
            - a war
            - seeing someone be killed or seriously injured
            - having a loved one die through homicide or suicide.
            Have you ever experienced this kind of event?""")
    if response == "no":
        window.destroy()
    else:
        window.destroy()
        PTSDtest.PTSD()


# anxiety

def anxiety():
    window.destroy()
    anxietytest.anxiety()


# display
# text1 = Label(window, text='Mental Health dfknvkldnvkTest',foreground="#000000",
#               font=intro_font)
# b = Listbox(window, selectmode='hi')


# b.pack(expand=YES, fill='both')


# main window
window = Tk()
window.title("mental health")
window.geometry("950x500")
window.resizable(False,False)
window.config(bg="#fff")


my_img=ImageTk.PhotoImage(Image.open("backpiccc.jpg"))
my_label=Label(image=my_img)
btn_depression = Button(window, text='depression', background='#000000',foreground="#ffffff",font=btn_font,
                        border=4, height=3, width=23, command=depression)

btn_anxiety = Button(window, text='anxiety',  background='#000000',foreground="#ffffff",font=btn_font,
                     border=4,height=3, width=23, command=anxiety)

btn_bipolar = Button(window, text='bipolar', background='#000000',foreground="#ffffff",font=btn_font,
                      border=4, height=3, width=23, command=bipolar)

btn_eatingdisorder = Button(window, text='ADHD'  ,background='#000000',foreground="#ffffff",font=btn_font,
                            border=4, height=3, width=23, command=ADHD)

btn_PTSD = Button(window, text='PTSD',  background='#000000',foreground="#ffffff",font=btn_font,
                   border=4,height=3, width=23, command=PTSD)

btn_schizophernia = Button(window, text='psychosis and schizophernia',
                            background='#000000',foreground="#ffffff",font=btn_font,
                             border=4, height=3, width=23, command=psychosis)


patientdatabase.create_table()
doctorDatabase.create_table()

# packing
my_label.pack()
# text1.pack()
btn_depression.pack()
btn_anxiety.pack()
btn_bipolar.pack()
btn_eatingdisorder.pack()
btn_PTSD.pack()
btn_schizophernia.pack()

# text1.place(x="250", y="50")
btn_depression.place(x="90", y="180")
btn_anxiety.place(x="90", y="330")
btn_bipolar.place(x="380", y="180")
btn_eatingdisorder.place(x="380", y="330")
btn_PTSD.place(x="670", y="180")
btn_schizophernia.place(x="670", y="330")

window.mainloop()
# print(write)
