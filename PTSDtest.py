from tkinter import *
from tkinter import ttk
import PatientInfo
import PTSDDatabase
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


def PTSD():
  
    counterq = 0
    questions = ["""1. had nightmares about the event(s) or thought about the event(s) 
when you did not want to?""",
                 """2. tried hard not to think about the event(s) or went out of your 
way to avoid situations that reminded you of the event(s)?""",
                 """3. been constantly on guard, watchful, or easily startled?""",
                 """4. felt numb or detached from people, activities, or your surroundings?""",
                 """5. felt guilty or unable to stop blaming yourself or others for 
the event(s) or any problems the event(s) may have caused?""",
                 ]

    def check():
        x = PTSDDatabase.total()
        write["result"] = x
        write["test_name"]="PTSD"
        windows[q].destroy()
        we=PatientInfo.information(write)
        
        tkinter.messagebox.showinfo(
            "Result", """Thank you for your time.The result will be handed to your doctor.""")
        
        
    def clicked(value):
        PTSDDatabase.result(value)
        # print(counterq)
        if counterq == 5:
            fbtn = Button(windows[q], text="NEXT", command=check,
                          font=nextbtn_font, background=nextbtn_color, width=13, border=4)
            fbtn.pack()
            fbtn.place(x="255",y="170")

    def clear():
        windows[q].destroy()
    
    windows = ["qwindow"+str(i) for i in range(len(questions))]
    for q in range(len(questions)):
            windows[q] = Tk()
            windows[q].geometry("700x300")
            windows[q].title("PTSD")
            windows[q].resizable(False,False)
            windows[q].grid_columnconfigure(0,weight=1)
            windows[q].config(bg=background_color)
            
            r = IntVar()
            r.set('0')
            intro = LabelFrame(
                windows[q], text="In the past month, have you...", font=question_font,background=question_color)
            ques = Label(intro, text=questions[q], font=question_font,background=question_color)
            btn_ch1 = Radiobutton(
                windows[q], text="Yes", font=question_font, variable=r, value=1, background=question_color,command=lambda: clicked(r.get()))
            btn_ch2 = Radiobutton(
                windows[q], text="No", variable=r, value=2, font=question_font, background=question_color,command=lambda: clicked(r.get()))
            
            counterq += 1
            if counterq <= 4:
                b = Button(windows[q], text="NEXT", command=clear,
                           font=nextbtn_font, background=nextbtn_color, width=13, border=4)
               
            
            intro.pack()
            ques.pack()
            ques.grid(row=2,column=0,sticky="w")
            btn_ch1.pack()
            btn_ch2.pack()
            b.pack()

            # intro.place(x="100",y="50")
            # ques.place(x="60",y="80")
            # btn_ch1.place(x="100",y="180")
            # btn_ch2.place(x="100",y="250")
            # b.place(x="255",y="170")
            windows[q].mainloop()
