from tkinter import *
from tkinter import ttk
import ADHDDatabase
import PatientInfo
import tkinter.messagebox


# font
submitbtn_font = ("Rockwell Extra Bold", 14)
question_font = ("Microsoft Sans Serif", 16)
nextbtn_font = ("Comic Sans MS", 15)

# color
nextbtn_color = "#999999"
question_color="#CCCCCC"
background_color="#CCCCCC"

write = dict()


def ADHD():
    counterq = 0
    questions = ["""1. How often do you have trouble wrapping up the final details 
of a project once the challenging parts have been done?""",
                 """2. How often do you have difficulty getting things 
in order when you have to do a task that requires organization?""",
                 """3. How often do you have problems remembering 
appointments or obligations?""",
                 """4. When you have a task that requires a lot of thought, 
how often do you avoid or delay getting started?""",
                 """5. How often do you fidget or squirm with your 
hands or feet when you have to sit down for a long time?""",
                 """6. How often do you feel overly active and compelled to 
do things,like you were driven by a motor?""",
                 """7. How often do you make careless mistakes when you have 
to work on a boring or difficult project?""",
                 """8. How often do you have difficulty keeping your 
attention when you are doing boring or repetitive work?""",
                 """9. How often do you have difficulty concentrating on what 
people say to you, even when they are speaking to you directly?""",
                 """10. How often do you misplace or have difficulty 
finding things at home or at work?""",
                 "11. How often are you distracted by activity or noise around you?",
                 """12. How often do you leave your seat in meetings or other 
situations in which you are expected to remain seated?""",
                 "13. How often do you feel restless or fidgety?",
                 """14. How often do you have difficulty unwinding 
and relaxing when you have time to yourself?""",
                 """15. How often do you find yourself talking 
too much when you are in social situations?""",
                 """16. When you're in a conversation, how often do you 
find yourself finishing the sentences of the people you 
are talking to, before they can finish them themselves?""",
                 """17. How often do you have difficulty waiting your turn in
situations when turn taking is required?""",
                 "18. How often do you interrupt others when they are busy?"]

    def check():
        x = ADHDDatabase.total()
        write["result"] = x
        write["test_name"]="ADHD"
        windows[q].destroy()
        we=PatientInfo.information(write)
        
        tkinter.messagebox.showinfo(
            "Result", """Thank you for your time.The result will be handed to your doctor.""")
        
        
        

    def clicked(value):
        ADHDDatabase.result(value)
        # print(counterq)
        if counterq == 18:
            fbtn = Button(windows[q], text="NEXT", command=check, width=13,
                          border=4, font=nextbtn_font, background=nextbtn_color)
            fbtn.pack()
            # depressionDatabase.total()
        # mylabe = Label(windows[q], text=value)
        # mylabe.pack()

    def clear():
        windows[q].destroy()

    windows = ["qwindow"+str(i) for i in range(len(questions))]
    for q in range(len(questions)):
        windows[q] = Tk()
        windows[q].geometry("700x350")
        windows[q].title("ADHD")
        windows[q].resizable(False,False)
        windows[q].grid_columnconfigure(0,weight=1)
        windows[q].config(bg=background_color)
        
        r = IntVar()
        r.set('0')
        intro=LabelFrame(windows[q],background=question_color)
        ques = Label(intro, text=questions[q], font=question_font,background=question_color)
        btn_ch1 = Radiobutton(
            intro, text="NEVER", font=question_font,background=question_color, variable=r, value=1, command=lambda: clicked(r.get()))
        btn_ch2 = Radiobutton(
            intro, text="RARELY", font=question_font,background=question_color, variable=r, value=2, command=lambda: clicked(r.get()))
        btn_ch3 = Radiobutton(
            intro, text="SOMETIMES", font=question_font,background=question_color, variable=r, value=3, command=lambda: clicked(r.get()))
        btn_ch4 = Radiobutton(
            intro, text="OFTEN", font=question_font,background=question_color, variable=r, value=4, command=lambda: clicked(r.get()))
        btn_ch5 = Radiobutton(
            intro, text="VERY OFTEN", font=question_font,background=question_color, variable=r, value=5, command=lambda: clicked(r.get()))
        # Label(windows[q], text=r.get()).pack()
        counterq += 1
        if counterq <= 17:
            b = Button(windows[q], text="NEXT", command=clear,width=13,
                          border=4,font=nextbtn_font, background=nextbtn_color)
        
        # packing
        intro.pack()
        ques.pack()
        btn_ch1.pack()
        btn_ch2.pack()
        btn_ch3.pack()
        btn_ch4.pack()
        btn_ch5.pack()
        b.pack()
        windows[q].mainloop()
