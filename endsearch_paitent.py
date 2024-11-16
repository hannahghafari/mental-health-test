from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import patientdatabase
import pandas as pd



# font
submitbtn_font = ("Comic Sans MS", 10)
question_font = ("Microsoft Sans Serif", 14)

# color
background_color="#CCCCCC"
search_color="#A689E1"
entry_color="#ede7f6"
btn_color = "#8B8B83"
quit_color="#D21404"



def end_task(result):
    

    # def 

    
    def clear(*clicked):
        if clicked:
            tree.selection_remove(tree.focus())
            tree.focus('')
        entry_id.delete(0,END)
        entry_fname.delete(0,END)
        entry_lname.delete(0,END)

    def display_data(event):
        selected_item=tree.focus()
        if selected_item:
            row=tree.item(selected_item)['values']
            clear()
            entry_id.insert(0,row[0])
            entry_fname.insert(0,row[1])
            entry_lname.insert(0,row[2])
        else:
            pass

    def next():
        id=entry_id.get()
        fname=entry_fname.get()
        lname=entry_lname.get()
        def delete():
            id=entry_id.get()
            fname=entry_fname.get()
            lname=entry_lname.get()
            print(id,fname,lname)
            res=patientdatabase.delete_patient(id,fname,lname)
            print(res)
            fwindow.destroy()

        if not (id and fname and lname):
            messagebox.showerror('Error','Enter all fields')
        else:
            fwindow=Tk()
            fwindow.geometry("1000x600")
            fwindow.config(bg=background_color)
            fwindow.resizable(False,False)
            fwindow.resizable(False,False)
            result=patientdatabase.fetch_SPpatient(id,fname,lname)
            print(result,type(result))
            print(result[0][1])
            name=result[0][2]+" "+ result[0][3]
            fwindow.title("{} result".format(name))
            # display
            
            pati = Label(fwindow, text="Information",background=background_color,
                    font=('Comic Sans MS', 36))

            name_pa = Label(fwindow, text="Name : {}".format(result[0][2]),
                            background=background_color,font=question_font)
            
            lname_pa = Label(fwindow, text="Last name : {}".format(result[0][3]),
                            background=background_color,font=question_font)
            
            test_pa = Label(fwindow, text="Test : {}".format(result[0][1]),
                            background=background_color,font=question_font)
            
            age_pa = Label(fwindow, text="Age : {}".format(result[0][4]),
                        background=background_color,font=question_font)
            
            gender_pa = Label(fwindow, text="Gender : {}".format(result[0][5]),
                            background=background_color,font=question_font)
            
            race_pa = Label(fwindow, text="Race : {}".format(result[0][6]),
                            background=background_color,font=question_font)
            
            job_pa = Label(fwindow, text="Job : {}".format(result[0][7]),
                        background=background_color,font=question_font)
            
            therapy_pa = Label(fwindow, text="Experience of therapy sessions: {}".format(result[0][8]),
                            background=background_color,font=question_font)
            
            mh_pa = Label(fwindow, text="Under any mental treatment : {}".format(result[0][9]),
                        background=background_color,font=question_font)
            
            ph_pa = Label(fwindow, text="Under any physical treatment: {}".format(result[0][10]),
                        background=background_color,font=question_font)
            
            date_pa = Label(fwindow, text="Date : {}".format(result[0][11]),
                            background=background_color,font=question_font)
            
            phone_pa = Label(fwindow, text="Phone number : {}".format(result[0][12]),
                            background=background_color,font=question_font)
            
            email_pa = Label(fwindow, text="Email : {}".format(result[0][13]),
                            background=background_color,font=question_font)
            
            result_pa = Label(fwindow, text="Result : {}".format(result[0][14]),
                            background=background_color,font=question_font)
            
            end_btn=Button(fwindow,text="Back",background=quit_color,font=question_font,
                        border=3,height=2,width=14,command=lambda:fwindow.destroy())
            delete_btn=Button(fwindow,text="Delete",background=search_color,font=question_font,
                        border=3,height=2,width=14,command=delete)
            
            # packing

            pati.pack()
            name_pa.pack()
            lname_pa.pack()
            phone_pa.pack()
            email_pa.pack()
            age_pa.pack()
            gender_pa.pack()
            race_pa.pack()
            job_pa.pack()
            test_pa.pack()
            therapy_pa.pack()
            mh_pa.pack()
            ph_pa.pack()
            date_pa.pack()
            result_pa.pack()
            end_btn.pack()
            delete_btn.pack()

            # placing
            pati.place(x="35",y="20")
            name_pa.place(x="35",y="130")
            lname_pa.place(x="35",y="160")
            age_pa.place(x="35",y="190")
            gender_pa.place(x="35",y="215")
            race_pa.place(x="35",y="245")
            job_pa.place(x="35",y="275")
            phone_pa.place(x="35",y="305")
            email_pa.place(x="35",y="335")
            result_pa.place(y="370")
            test_pa.place(x="560",y="130")
            therapy_pa.place(x="560",y="160")
            mh_pa.place(x="560",y="190")
            ph_pa.place(x="560",y="215")
            date_pa.place(x="560",y="245")
            
            delete_btn.place(x="280",y="470")
            end_btn.place(x="470",y="470")

            fwindow.mainloop()

    
    
    #main window
    info = Tk()
    info.title("Search...")
    info.config(bg=background_color)
    
    # create the input frame
    input_frame = tk.Frame(info)
    input_frame.pack(pady=10)

     # create entry and label
    label_id = tk.Label(input_frame, text="ID :")
    label_id.grid(row=0, column=0)
    
    entry_id = tk.Entry(input_frame)
    entry_id.grid(row=0, column=1)

    label_fname = tk.Label(input_frame, text="First name :")
    label_fname.grid(row=0, column=2)
    
    entry_fname = tk.Entry(input_frame)
    entry_fname.grid(row=0, column=3)

    label_lname = tk.Label(input_frame, text="Last name :")
    label_lname.grid(row=0, column=4)
    
    entry_lname = tk.Entry(input_frame)
    entry_lname.grid(row=0, column=5)

    # ایجاد Treeview و Scrollbar
    tree_frame = tk.Frame(info)
    tree_frame.pack(expand=True, fill='both')

    tree = ttk.Treeview(tree_frame)

    # defining columns
    tree["columns"] = list(result.columns)
    # only show headings
    tree["show"] = "headings" 

     # adjust columns width
    for col in result.columns:
        # adjust each column width
        tree.column(col, width=100) 
        # heading of each column
        tree.heading(col, text=col) 

     # Treeview
    for index, row in result.iterrows():
        tree.insert("", "end", values=list(row))

    # scrollbar
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # put scrollbar in treeview
    tree.pack(side=tk.LEFT, expand=True, fill='both')
    scrollbar.pack(side=tk.RIGHT, fill='y')

    # create buttons
    button_frame = tk.Frame(info)
    button_frame.pack(pady=10)
    search_button = tk.Button(button_frame, text="Next", background=search_color,font=submitbtn_font,
                        cursor='hand2',border=3, height=2, width=12, command=next)
    search_button.grid(row=0, column=0, padx=5)


    quit_button = tk.Button(button_frame, text="Quit",background=quit_color,font=submitbtn_font,
                        cursor='hand2',border=3, height=2, width=12, command=lambda:info.destroy())
    quit_button.grid(row=0, column=1, padx=5)

    tree.bind('<ButtonRelease>',display_data)

    

    info.mainloop()
