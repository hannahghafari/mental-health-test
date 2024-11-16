from tkinter import *
from tkinter import ttk
import PatientInfo
import psychosisDatabase
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


def psychosis():
    counterq = 0
    questions = ["""1. Do familiar surroundings sometimes seem strange, confusing, 
threatening or unreal to you?""",
                 """2. Have you heard unusual sounds like banging,clicking, hissing,
clapping or ringing in your ears?""",
                 """3. Do things that you see appear different from the way they usually do?""",
                 """4. Have you had experiences with telepathy, psychic forces, or fortune telling?""",
                 """5. Have you felt that you are not in control of your own ideas or thoughts?""",
                 """6. Do you have difficulty getting your point across, because you
ramble or go off the track a lot when you talk?""",
                 """7. Do you have strong feelings or beliefs about being unusually 
gifted or talented in some way?""",
                 """8. Do you feel that other people are watching you or talking about you?""",
                 """9. Do you sometimes get strange feelings on or just beneath your skin,
like bugs crawling?""",
                 """10. Do you sometimes feel suddenly distracted by distant sounds 
that you are not normally aware of?""",
                 """11. Have you had the sense that some person or force is around 
you, although you couldn't see anyone?""",
                 """12. Do you worry at times that something may be wrong with your mind?""",
                 """13. Have you ever felt that you don't exist, the world does not
exist, or that you are dead?""",
                 """14. Have you been confused at times whether something you 
experienced was real or imaginary?""",
                 """15. Do you hold beliefs that other people would find unusual or bizarre?""",
                 """16. Do you feel that parts of your body have changed in some way,
or that parts of your body are working differently?""",
                 """17. Are your thoughts sometimes so strong that you can almost hear them?""",
                 """18. Do you find yourself feeling mistrustful or suspicious of other people?""",
                 """19. Have you seen unusual things like flashes, flames, blinding light,
or geometric figures?""",
                 """20. Have you seen things that other people can't see or don't seem to see?""",
                 """21. Do people sometimes find it hard to understand what you are saying?"""]

    def check():
        x = psychosisDatabase.total()
        write["result"] = x
        write["test_name"]="Psychosis and schizophernia"
        windows[q].destroy()
        we=PatientInfo.information(write)
        
        tkinter.messagebox.showinfo(
            "Result", """Thank you for your time.The result will be handed to your doctor.""")
        
       

    def clicked(value):
        psychosisDatabase.result(value)
        # print(counterq)
        if counterq == 21:
            fbtn = Button(windows[q], text="NEXT", command=check,
                          font=nextbtn_font, background=nextbtn_color, width=13, border=4)
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
        windows[q].title("psychosis")
        windows[q].resizable(False,False)
        windows[q].grid_columnconfigure(0,weight=1)
        windows[q].config(bg=background_color)
            
        
        r = IntVar()
        r.set('0')
        intro = LabelFrame(
            windows[q], text="""Over the past 2 weeks,how often have you been bothered by ...""", font=question_font,background=background_color)
        
        ques = Label(intro,background=background_color, text=questions[q], font=question_font)
        btn_ch1 = Radiobutton(
            intro,background=background_color, text="Yes", font=question_font, variable=r, value=1, command=lambda: clicked(r.get()))
        btn_ch2 = Radiobutton(
            intro,background=background_color, text="No", font=question_font, variable=r, value=2, command=lambda: clicked(r.get()))
        # Label(windows[q], text=r.get()).pack()
        counterq += 1
        if counterq <= 20:
            b = Button(windows[q], text="NEXT", command=clear,
                       font=nextbtn_font, background=nextbtn_color, width=13, border=4)
        intro.pack()
        ques.pack()
        btn_ch1.pack()
        btn_ch2.pack()
        b.pack()
        windows[q].mainloop()
