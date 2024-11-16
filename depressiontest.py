from tkinter import *
from tkinter import ttk
import depressionDatabase
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


def depression():

    counterq = 0
    questions = ["1. Little interest or pleasure in doing things",
                 "2. Feeling down, depressed, or hopeless",
                 "3. Trouble falling or staying asleep, or sleeping too much",
                 "4. Feeling tired or having little energy",
                 "5. Poor appetite or overeating",
                 """6. Feeling bad about yourself - or that you are a failure 
or have let yourself or your family down""",
                 """7. Trouble concentrating on things, such as reading newspaper 
or watching television""",
                 """8. Moving or speaking so slowly that other people could have 
noticed Or the opposite - being so fidgety or restless that you 
have been moving around a lot more than usual""",
                 "9. Thoughts that you would be better off dead, or of hurting yourself"]

    def check():
        x = depressionDatabase.total()
        write["result"] = x
        write["test_name"]="depression"
        windows[q].destroy()
        we=PatientInfo.information(write)
        
        tkinter.messagebox.showinfo(
            "Result", """Thank you for your time.The result will be handed to your doctor.""")

    def clicked(value):
        depressionDatabase.result(value)
        # print(counterq)
        if counterq == 9:
            fbtn = Button(windows[q], text="NEXT", command=check,
                          border=4, font=nextbtn_font, background=nextbtn_color, width=13)
            fbtn.pack()
            # depressionDatabase.total()
        # mylabe = Label(windows[q], text=value)
        # mylabe.pack()

    def clear():
        windows[q].destroy()

    windows = ["qwindow"+str(i) for i in range(len(questions))]
    # window.destroy()
    for q in range(len(questions)):
        windows[q] = Tk()
        windows[q].geometry("800x350")
        windows[q].title("depression")
        windows[q].resizable(False,False)
        windows[q].grid_columnconfigure(0,weight=1)
        windows[q].config(bg=background_color)
            

        r = IntVar()
        r.set('0')
        intro = LabelFrame(
            windows[q], background=question_color, text="""Over the past 2 weeks,how often have you been bothered by...""", font=question_font)
        ques = Label(intro, background=question_color, text=questions[q], font=question_font)
        btn_ch1 = Radiobutton(
            intro, background=question_color, text="NOT AT ALL", font=question_font, variable=r, value=1, command=lambda: clicked(r.get()))
        btn_ch2 = Radiobutton(
            intro, background=question_color, text="SEVERAL DAYS", font=question_font, variable=r, value=2, command=lambda: clicked(r.get()))
        btn_ch3 = Radiobutton(
           intro, background=question_color, text="MORE THAN HALF THE DAYS", font=question_font, variable=r, value=3, command=lambda: clicked(r.get()))
        btn_ch4 = Radiobutton(
            intro, background=question_color, text="NEARLY EVERY DAY", font=question_font, variable=r, value=4, command=lambda: clicked(r.get()))
        # Label(windows[q], text=r.get()).pack()
        counterq += 1
        if counterq <= 8:
            b = Button(windows[q], text="NEXT", command=clear,
                       border=4, font=nextbtn_font, background=nextbtn_color, width=13)
        
        # packing
        intro.pack()
        ques.pack()
        btn_ch1.pack()
        btn_ch2.pack()
        btn_ch3.pack()
        btn_ch4.pack()
        b.pack()
        windows[q].mainloop()