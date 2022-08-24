from tkinter import *
import random
import time

root = Tk()

root.geometry("1600x800+0+0")
root.title("Restaurant Management System by Charles Adure")

Top = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Top.pack(side=TOP)

f1 = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

#====================== App Title Name ======================
title_main = Label(Top, font=('arial', 50, 'bold'), text='RESTAURANT MANAGEMENT SYSTEM', fg='steel blue', bd=10, anchor='w')
title_main.grid(row=0, column=0)

#====================== Time ================================
localtime = time.asctime(time.localtime(time.time()))
title_main = Label(Top, font=('arial', 20, 'italic'), text=localtime, fg='steel blue', bd=10, anchor='w')
title_main.grid(row=1, column=0)

#======================= Calculator =========================
text_input = StringVar()
operator = ""

def btn_click(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def btn_clear_action():
    global operator
    operator = ""
    text_input.set("")

Calc_display = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_input, insertwidth=4, bg='powder blue',
                     bd=20, justify='right')
Calc_display.grid(columnspan=4)

#========================= Row2 =========================================
btn7 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='7', command=lambda: btn_click(7))
btn7.grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='8', command=lambda: btn_click(8))
btn8.grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='9', command=lambda: btn_click(9))
btn9.grid(row=2, column=2)
Addition = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='+', command=lambda: btn_click('+'))
Addition.grid(row=2, column=3)

#============================= Row3 ========================

btn4 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='4', command=lambda: btn_click(4))
btn4.grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='5', command=lambda: btn_click(5))
btn5.grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='6', command=lambda: btn_click(6))
btn6.grid(row=3, column=2)
Subtraction = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='-', command=lambda: btn_click('-'))
Subtraction.grid(row=3, column=3)

#============================= Row3 ========================

btn1 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='1', command=lambda: btn_click(1))
btn1.grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='2', command=lambda: btn_click(2))
btn2.grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='3', command=lambda: btn_click(3))
btn3.grid(row=4, column=2)
multiplication = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='*', command=lambda: btn_click('*'))
multiplication.grid(row=4 , column=3)

#============================= Row3 ========================

btn0 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='0', command=lambda: btn_click(0))
btn0.grid(row=5, column=0)
btn_clear = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='C', command=btn_clear_action)
btn_clear.grid(row=5, column=1)
btn_equalto = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='=')
btn_equalto.grid(row=5, column=2)
division = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='/', command=lambda: btn_click('/'))
division.grid(row=5, column=3)

root.mainloop()