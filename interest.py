from tkinter import *
window=Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='#252525')

def calculateIneterest():
    p = int(principal.get())
    t = int(period.get())
    r = int(rate.get())

    i = (p*t*r)/100

    i = round(i,2)

    name = username.get()

    result_label.destroy()

    final_msg = Label(result_frame,text=name+", your interest amount is Rs."+str(i),fg="white",bg="#252525",font=("Calibri",12),bd=1)
    final_msg.place(x=20,y=20)
    final_msg.pack()




app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "white", bg = "#252525", font=("Calibri", 20),bd=5)
app_label.place(x=15, y=20)

name_label=Label(window, text="Your Name :", fg = "white", bg = "#252525", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=200, y=92)

principal_label = Label(window,text="Principal Amount (Rs):",fg="white",bg="#252525",font=("Calibri",12),bd=1)
principal_label.place(x=20,y=140)

principal = Entry(window,text="",bd=2,width=22)
principal.place(x=200,y=142)

period_label = Label(window,text="Period (Yrs):",fg="white",bg="#252525",font=("Calibri",12),bd = 1)
period_label.place(x=20,y=190)

period = Entry(window,text="",bd=2,width=22)
period.place(x=200,y=192)

rate_label = Label(window,text="Rate of Interest (p.c.p.a) :",fg="white",bg="#252525",font=("Calibri",12),bd = 1)
rate_label.place(x=20,y=240)

rate = Entry(window,text="",bd=2,width=22)
rate.place(x=200,y=242)

button = Button(window,text="Calculate",fg="black",bg="#868686",command=calculateIneterest)
button.place(x=20,y=290)

result_frame = LabelFrame(window,text="Result",fg="white", bg = "#252525", font=("Calibri", 12))
result_frame.place(x=20,y=340)

result_label=Label(result_frame,text=" ",fg="white", bg = "#252525", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()
