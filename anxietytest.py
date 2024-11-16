from tkinter import *
from tkinter import ttk
import PatientInfo
import anxietyDatabase
import tkinter.messagebox


# font
submitbtn_font = ("Rockwell Extra Bold", 14)
question_font = ("Microsoft Sans Serif", 16)
nextbtn_font = ("Comic Sans MS", 15)
intro_font=("Microsoft Sans Serif", 14)

# color
nextbtn_color = "#999999"
question_color="#CCCCCC"
background_color="#CCCCCC"


write = dict()

def anxiety():
    counterq = 0
    questions = ["1. Feeling nervous, anxious, or on edge",
                 "2. Not being able to stop or control worrying",
                 "3. Worrying too much about different things",
                 "4. Trouble relaxing",
                 "5. Being so restless that it is hard to sit still",
                 "6. Becoming easily annoyed or irritable",
                 "7. Feeling afraid, as if something awful might happen"]

    def check():
        x = anxietyDatabase.total()
        write["result"] = x
        write["test_name"]="anxiety"
        windows[q].destroy()
        we=PatientInfo.information(write)

        tkinter.messagebox.showinfo(
            "Result", """Thank you for your time.The result will be handed to your doctor.""")
        
        
    def clicked(value):
        anxietyDatabase.result(value)
        # print(counterq)
        if counterq == 7:
            fbtn = Button(windows[q], text="NEXT", command=check,
                          font=nextbtn_font, background=nextbtn_color, width=13, border=4)
            fbtn.pack()
            fbtn.place(x="300",y="220")
            # depressionDatabase.total()
        # mylabe = Label(windows[q], text=value)
        # mylabe.pack()

    def clear():
        windows[q].destroy()

    windows = ["qwindow"+str(i) for i in range(len(questions))]
    for q in range(len(questions)):
        windows[q] = Tk()
        windows[q].geometry("800x300")
        windows[q].title("Anxiety")
        windows[q].resizable(False,False)
        windows[q].grid_columnconfigure(0,weight=1)
        windows[q].config(bg=background_color)


        r = IntVar()
        r.set('0')
        intro = LabelFrame(
            windows[q], text="""Over the last 2 weeks, how often have you been bothered by the following problems....""", font=intro_font,background=question_color)
        ques = Label(intro, text=questions[q], font=question_font,background=question_color)
        btn_ch1 = Radiobutton(
            intro,background=question_color, text="NOT AT ALL", font=question_font, variable=r, value=1, command=lambda: clicked(r.get()))
        btn_ch2 = Radiobutton(
           intro,background=question_color, text="SEVERAL DAYS", font=question_font, variable=r, value=2, command=lambda: clicked(r.get()))
        btn_ch3 = Radiobutton(
            intro,background=question_color, text="MORE THAN HALF THE DAYS", font=question_font, variable=r, value=3, command=lambda: clicked(r.get()))
        btn_ch4 = Radiobutton(
           intro,background=question_color, text="NEARLY EVERY DAY", font=question_font, variable=r, value=4, command=lambda: clicked(r.get()))
        # Label(windows[q], text=r.get()).pack()
        counterq += 1
        if counterq <= 6:
            b = Button(windows[q], text="NEXT", command=clear,
                       font=nextbtn_font, background=nextbtn_color, width=13, border=4)
            b.pack()
            b.place(x="300",y="220")
        # packing
        intro.pack()
        ques.pack()
        btn_ch1.pack()
        btn_ch2.pack()
        btn_ch3.pack()
        btn_ch4.pack()
        windows[q].mainloop()


