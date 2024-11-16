from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import patientdatabase
import endsearch_paitent
import pandas as pd


# font
submitbtn_font = ("Comic Sans MS", 14)
question_font = ("Microsoft Sans Serif", 14)

# color
background_color="#CCCCCC"
submitbtn_color = "#999999"

    


def dc():
    # functions 
    
    def search():
        test_name=testname.get()
        gender1=Gender.get()
        race1=Race.get()
        if not (test_name and gender1 and race1):
            messagebox.showerror('Error','Enter all fields')
        else:
            result=patientdatabase.search_patient(test_name,gender1,race1)
            chart=pd.DataFrame(result)
            chart.rename(columns={0: "ID"}, inplace=True)
            chart.rename(columns={1: "First name"}, inplace=True)
            chart.rename(columns={2: "Last name"}, inplace=True)
            window.destroy()
            endsearch_paitent.end_task(chart)
        
    
    # main window

    window=Tk()
    window.title('Search...')
    window.geometry('500x370')
    window.config(bg=background_color)
    window.resizable(False,False)
    

    # labels & entries
    searchfield=LabelFrame(window, text='Search Range...',background=background_color,
              font=('Comic Sans MS', 36))
    
    testname_label=Label(searchfield,text="Test name",background=background_color,font=question_font)
    testname= StringVar()
    testname.set('_________')
    Test_entry=OptionMenu(searchfield,testname,"ADHD","PTSD","psychosis","depression","bipolar","anxiety")

    Gender_label=Label(searchfield,text="Gender",background=background_color,font=question_font)
    Gender = StringVar()
    Gender.set('_________')
    genderr=OptionMenu(searchfield,Gender,"female","male")

    race_label=Label(searchfield,text="Race:",background=background_color,font=question_font)
    Race = StringVar()
    Race.set("__________")
    racee = OptionMenu(searchfield, Race, "Asian", "American","European","African")


    # buttons
    search_button=Button(window,text="Search Patient",background=submitbtn_color,font=submitbtn_font,
                         cursor='hand2',border=3, height=2, width=12,command=search)


    # packing
    searchfield.pack()
    testname_label.pack()
    Test_entry.pack()
    Gender_label.pack()
    genderr.pack()
    race_label.pack()
    racee.pack()
    search_button.pack()
    # placing
    search_button.place(x="170",y="260")

    window.mainloop()
