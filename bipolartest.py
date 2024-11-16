from tkinter import *
from tkinter import ttk
import PatientInfo
import bipolarDatabase
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



def bipolar():
    counterq = 0
    questions = ["""1. You felt so good or hyper that other people thought you were not your normal
self or were so hyper that you got into trouble?""",
                 "2. You were so irritable that you shouted at people or started fights or arguments?",
                 "3. You felt much more self-confident than usual?",
                 "4. You got much less sleep than usual and found you didn't really miss it?",
                 "5. You were much more talkative or spoke much faster than usual?",
                 "6. Thoughts raced through your head or you couldn't slow your mind down?",
                 """7. You were so easily distracted by things 
around you that you had trouble concentrating or staying on track?""",
                 "8. You had much more energy than usual?",
                 """9. You were much more social or outgoing than usual, 
for example, you telephoned friends in the middle of the night?""",
                 "10. You were much more interested in sex than usual?",
                 """11. You did things that were unusual for you or that 
other people might have thought were excessive, foolish, or risky?""",
                 "12. Spending money got you or your family into trouble?"]

    def check():
        x = bipolarDatabase.total()
        write["result"] = x
        write["test_name"]="bipolar"
        windows[q].destroy()
        we=PatientInfo.information(write)
        
        tkinter.messagebox.showinfo(
            "Result", """Thank you for your time.The result will be handed to your doctor.""")
        
        
    def clicked(value):
        bipolarDatabase.result(value)
        # print(counterq)
        if counterq == 12:
            fbtn = Button(windows[q], text="NEXT", command=check,
                          font=nextbtn_font, background=nextbtn_color, border=4, width=13)
            fbtn.pack()
            # depressionDatabase.total()
        # mylabe = Label(windows[q], text=value)
        # mylabe.pack()

    def clear():
        windows[q].destroy()

    windows = ["qwindow"+str(i) for i in range(len(questions))]
    for q in range(len(questions)):
        windows[q] = Tk()
        windows[q].geometry("800x300")
        windows[q].title("Bipolar")
        windows[q].resizable(False,False)
        windows[q].grid_columnconfigure(0,weight=1)
        windows[q].config(bg=background_color)
            
        r = IntVar()
        r.set('0')
        intro = LabelFrame(
            windows[q],background=question_color, text="Has there ever been a period of time when you were not your usual self and...", font=question_font)
        
        ques = Label(intro,background=question_color, text=questions[q], font=question_font)
        btn_ch1 = Radiobutton(
            intro,background=question_color, text="Yes", variable=r, value=1, font=question_font, command=lambda: clicked(r.get()))
        btn_ch2 = Radiobutton(
            intro,background=question_color, text="No", variable=r, value=2, font=question_font, command=lambda: clicked(r.get()))
        # Label(windows[q], text=r.get()).pack()
        counterq += 1
        if counterq <= 11:
            b = Button(windows[q], text="NEXT", command=clear, border=4,
                       font=nextbtn_font, background=nextbtn_color, width=13)
        
        # packing
        intro.pack()
        ques.pack()
        btn_ch1.pack()
        btn_ch2.pack()
        b.pack()
        windows[q].mainloop()
