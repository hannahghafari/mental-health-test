from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import patientdatabase
from datetime import datetime

# font
submitbtn_font = ("Comic Sans MS", 15)
question_font = ("Microsoft Sans Serif", 14)
intro_font=("Microsoft Sans Serif", 14)

# color
question_color="#CCCCCC"
background_color="#CDCDB4"
submitbtn_color = "#8B8B7A"
entry_color="#ede7f6"


def information(write):
    second_frame = Tk()
    second_frame.config(bg=background_color)
    second_frame.geometry("900x550")
    second_frame.title("Information")
    second_frame.resizable(False,False)
    

    # border
    Pinfo=LabelFrame(second_frame,text="Personal information",background=background_color,font=question_font)
    Pbackground=LabelFrame(second_frame,text="Medical background",background=background_color,font=question_font)
    
    # labels
    nameentry = Label(Pinfo, text="Enter your name",background=background_color,font=question_font)
    lnameentry = Label(Pinfo, text="Enter your last name",background=background_color,font=question_font)
    ageentry = Label(Pinfo, text="Enter your age",background=background_color,font=question_font)
    genderentery = Label(Pinfo, text="Enter your gender",background=background_color,font=question_font)
    jobentry = Label(Pinfo, text="what do you do?",background=background_color,font=question_font)
    raceentry = Label(Pinfo, text="Enter your race",background=background_color,font=question_font)
    emailentry = Label(Pinfo, text="Enter your Email",background=background_color,font=question_font)
    phonenumberentry = Label(Pinfo, text="  Enter your phone number  ",background=background_color,font=question_font)
    physicalQ = Label(
        Pbackground, text="Are you under any medical treatment for physical health?",background=background_color,font=question_font)
    mentalQ = Label(
        Pbackground, text="Are you under any medical treatment for mental health?",background=background_color,font=question_font)
    therapy = Label(Pbackground, text="Have you ever had a therapy session?",background=background_color,font=question_font)


    # entries
    Pemail = Entry(Pinfo, width=22,background=entry_color)
    Pjob = Entry(Pinfo, width=22,background=entry_color)    
    Pphone_number = Entry(Pinfo, width=22,background=entry_color)
    name = Entry(Pinfo, width=22,background=entry_color)
    lname = Entry(Pinfo, width=22,background=entry_color)
    Page = Entry(Pinfo, width=22,background=entry_color)

    Pgender = StringVar()
    Pgender.set('0')
    genderf = Radiobutton(Pinfo,font=question_font, text="Female", variable=Pgender,background=background_color,
                          value="female", command=lambda: clickedG(Pgender.get()))
    genderm = Radiobutton(Pinfo,font=question_font, text="Male", variable=Pgender,background=background_color,
                          value="male", command=lambda: clickedG(Pgender.get()))


    Prace = StringVar()
    Prace.set("________")
    racee = OptionMenu(Pinfo, Prace, "Asian", "American", "African","European")

    phe = StringVar()
    phe.set("0")
    phY = Radiobutton(Pbackground,font=question_font, text="Yes", variable=phe,background=background_color,
                      value="Yes", command=lambda: clickedPH(phe.get()))
    phN = Radiobutton(Pbackground,font=question_font, text="No", variable=phe,background=background_color,
                      value="No", command=lambda: clickedPH(phe.get()))

    mhe = StringVar()
    mhe.set("0")
    mhY = Radiobutton(Pbackground,font=question_font, text="Yes", variable=mhe,background=background_color,
                      value="Yes", command=lambda: clickedMH(mhe.get()))
    mhN = Radiobutton(Pbackground,font=question_font, text="No", variable=mhe,background=background_color,
                      value="No", command=lambda: clickedMH(mhe.get()))
    
    therapye = StringVar()
    therapye.set('0')
    therapyY = Radiobutton(Pbackground,font=question_font, text="Yes", variable=therapye,background=background_color,
                          value="Yes", command=lambda: clickedT(therapye.get()))
    therapyN = Radiobutton(Pbackground,font=question_font, text="No", variable=therapye,background=background_color,
                          value="No", command=lambda: clickedT(therapye.get()))
    
    
    
    
    # functions
    def clickedG(Pgender):
        write["gender"] = Pgender

    def clickedPH(condition):
        write["physical_health_issue"] = condition

    def clickedMH(condition):
        write["mental_health_issue"] = condition

    def clickedT(condition):
        write["therapy_session"] = condition

    def insert():
        patientdatabase.create_table()
        date = "{}".format(datetime.now().strftime("%B %d %Y"))
        gender=write["gender"]
        print(gender,type(gender))
        physical_health_issue=write["physical_health_issue"]
        mental_health_issue=write["mental_health_issue"]
        therapy_session=write["therapy_session"]
        test_name=write["test_name"]
        result=write["result"]
        id=patientdatabase.get_id()
        print(id,type(id))
        first_name = name.get()
        last_name = lname.get()
        age = Page.get()
        job_info = Pjob.get()
        race = Prace.get()
        email = Pemail.get()
        phone_number = Pphone_number.get()
        if not (first_name and last_name and age and job_info and race and email and phone_number):
                messagebox.showerror('Error','Enter all fields')
        else:
            patientdatabase.insert_patient(id,test_name,first_name,last_name,age,gender,race,job_info,therapy_session,mental_health_issue,physical_health_issue,date,phone_number,email,result)
            second_frame.destroy()
            second_frame.destroy()
        # write["name"] = Pname
        # write["last_name"] = Plname
        # write["age"] = Page
        # write["job_info"] = Pjob
        # write["race"] =Prace
        # write["email"] = Pemail
        # write["phone_number"] = Pnumber
        

        # print(write)
        

        
        
        
    finish_btn = Button(second_frame, font=submitbtn_font, width=13, border=4,
                      background=submitbtn_color, text="FINISH", command=insert)
    

    # packing
    Pinfo.pack()
    nameentry.pack()
    name.pack()
    lnameentry.pack()
    lname.pack()
    ageentry.pack()
    Page.pack()
    genderentery.pack()
    genderf.pack()
    genderm.pack()
    jobentry.pack()
    Pjob.pack()
    raceentry.pack()
    racee.pack()
    emailentry.pack()
    Pemail.pack()
    phonenumberentry.pack()
    Pphone_number.pack()
    Pbackground.pack()
    physicalQ.pack()
    phY.pack()
    phN.pack()
    mentalQ.pack()
    mhY.pack()
    mhN.pack()
    # mhY.pack()
    therapy.pack()
    therapyY.pack()
    therapyN.pack()
    finish_btn.pack()
    
    # placing
    Pinfo.place(x="45",y="30")
    Pbackground.place(x="350",y="30")
    finish_btn.place(x="493",y="410")

    second_frame.mainloop()
    return write




