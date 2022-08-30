from tkinter import *
import random
import time

root = Tk()

root.geometry("1600x800+0+0")
root.title("Restaurant Management System by Charles Adure")

Top = Frame(root, width=1600, height=50, bg="dark blue", relief=SUNKEN)
Top.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#====================== App Title Name ======================
title_main = Label(Top, font=('arial', 50, 'bold'), text='RESTAURANT MANAGEMENT SYSTEM', fg='steel blue', bd=10,
                   anchor='w')
title_main.grid(row=0, column=0)

#====================== Time ================================
localtime = time.asctime(time.localtime(time.time()))
title_main = Label(Top, font=('arial', 20, 'italic'), text=localtime, fg='steel blue', bd=10, anchor='w')
title_main.grid(row=1, column=0)

#======================= Calculator and all functions/methods =========================
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

def btn_equalto_action():
    global operator
    result = str(eval(operator))
    text_input.set(result)
    operator = ""

def TotalButton():
    x = random.randint(10387, 500283)
    randomTotalButton = str(x)
    rand.set(randomTotalButton)

    NoJollof = float(jollof.get())
    NoFriedRice = float(fried.get())
    NoChicken = float(chicken.get())
    NoTurkey = float(turkey.get())
    NoPlantain = float(plantain.get())
  #  NoFriedFish = float(friedfish.get())
    NoSoftDrink = float(softdrink.get())
    NoWater = float(water.get())
    NoWine = float(wine.get())

    costofjollof = NoJollof * 1200
    costoffriedrice = NoFriedRice * 1200
    costofchicken = NoChicken * 2500
    costofturkey = NoTurkey * 2200
    costofplantain = NoPlantain * 400
 #   costoffriedfish = NoFriedFish * 1500
    costofsoftdrink = NoSoftDrink * 300
    costofwater = NoWater * 200
    costofwine = NoWine * 3000

    CostofMeal = '₦', str('%.2f' % (costofjollof + costoffriedrice + costofchicken + costofturkey + costofplantain
                                    + costofsoftdrink + costofwater + costofwine))
    Tax = (costofjollof + costoffriedrice + costofchicken + costofturkey + costofplantain
           + costofsoftdrink + costofwater + costofwine) * 0.075
    MealCost = (costofjollof + costoffriedrice + costofchicken + costofturkey + costofplantain
                + costofsoftdrink + costofwater + costofwine)

    Tax_pay = '₦', str('%.2f' % (Tax))
    Meal_sum_total = '₦', str('%.2f' % (Tax + MealCost))

    taxcost.set(Tax_pay)
    subtotal.set(CostofMeal)
    totalcost.set(Meal_sum_total)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    jollof.set("")
    fried.set("")
    chicken.set("")
    turkey.set("")
    plantain.set("")
    friedfish.set("")
    softdrink.set("")
    water.set("")
    wine.set("")
    subtotal.set("")
    totalcost.set("")

rand = StringVar()
jollof = StringVar()
fried = StringVar()
chicken = StringVar()
turkey = StringVar()
plantain = StringVar()
#friedfish = StringVar()
softdrink = StringVar()
water = StringVar()
wine = StringVar()
subtotal = StringVar()
totalcost = StringVar()
taxcost = StringVar()


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
             text='=', command=btn_equalto_action)
btn_equalto.grid(row=5, column=2)
division = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), bg='powder blue', fg='black', bd=8,
             text='/', command=lambda: btn_click('/'))
division.grid(row=5, column=3)

#-------------------------------- Menu ---------------------------------------

label_reference = Label(f1, font=('arial', 20, 'bold'), text='Reference', fg='black',
                        bd=16, anchor='w')
label_reference.grid(row=0, column=0)
entry_reference = Entry(f1, font=('arial', 20, 'bold'), textvariable=rand, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_reference.grid(row=0, column=1)

jollof_rice = Label(f1, font=('arial', 20, 'bold'), text='Jollof Rice', fg='black',
                        bd=16, anchor='w')
jollof_rice.grid(row=1, column=0)
entry_jollof = Entry(f1, font=('arial', 20, 'bold'), textvariable=jollof, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_jollof.grid(row=1, column=1)

fried_rice = Label(f1, font=('arial', 20, 'bold'), text='Fried Rice', fg='black',
                        bd=16, anchor='w')
fried_rice.grid(row=2, column=0)
entry_fried_rice = Entry(f1, font=('arial', 20, 'bold'), textvariable=fried, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_fried_rice.grid(row=2, column=1)

fried_chicken = Label(f1, font=('arial', 20, 'bold'), text='Fried Chicken', fg='black',
                        bd=16, anchor='w')
fried_chicken.grid(row=3, column=0)
entry_fried_chicken = Entry(f1, font=('arial', 20, 'bold'), textvariable=chicken, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_fried_chicken.grid(row=3, column=1)

fried_turkey = Label(f1, font=('arial', 20, 'bold'), text='Fried Turkey', fg='black',
                        bd=16, anchor='w')
fried_turkey.grid(row=4, column=0)
entry_fried_turkey = Entry(f1, font=('arial', 20, 'bold'), textvariable=turkey, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_fried_turkey.grid(row=4, column=1)

fried_plantain = Label(f1, font=('arial', 20, 'bold'), text='Fried Plantain', fg='black',
                        bd=16, anchor='w')
fried_plantain.grid(row=5, column=0)
entry_fried_plantain = Entry(f1, font=('arial', 20, 'bold'), textvariable=plantain, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_fried_plantain.grid(row=5, column=1)

soft_drinks = Label(f1, font=('arial', 20, 'bold'), text='Soft Drinks', fg='black',
                        bd=16, anchor='w')
soft_drinks.grid(row=0, column=2)
entry_soft_drinks = Entry(f1, font=('arial', 20, 'bold'), textvariable=softdrink, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_soft_drinks.grid(row=0, column=3)

Water = Label(f1, font=('arial', 20, 'bold'), text='Water', fg='black',
                        bd=16, anchor='w')
Water.grid(row=1, column=2)
entry_water = Entry(f1, font=('arial', 20, 'bold'), textvariable=water, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_water.grid(row=1, column=3)

Wine = Label(f1, font=('arial', 20, 'bold'), text='Wine', fg='black',
                        bd=16, anchor='w')
Wine.grid(row=2, column=2)
entry_wine = Entry(f1, font=('arial', 20, 'bold'), textvariable=wine, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_wine.grid(row=2, column=3)

Sub_total = Label(f1, font=('arial', 20, 'bold'), text='Sub Total', fg='black',
                        bd=16, anchor='w')
Sub_total.grid(row=3, column=2)
entry_subtotal = Entry(f1, font=('arial', 20, 'bold'), textvariable=subtotal, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_subtotal.grid(row=3, column=3)

Tax_cost = Label(f1, font=('arial', 20, 'bold'), text='Tax', fg='black',
                        bd=16, anchor='w')
Tax_cost.grid(row=4, column=2)
entry_tax_cost = Entry(f1, font=('arial', 20, 'bold'), textvariable=taxcost, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_tax_cost.grid(row=4, column=3)

Total_cost = Label(f1, font=('arial', 20, 'bold'), text='Total Cost', fg='black',
                        bd=16, anchor='w')
Total_cost.grid(row=5, column=2)
entry_total_cost = Entry(f1, font=('arial', 20, 'bold'), textvariable=totalcost, bd=10,
                        fg='black', insertwidth=2, justify='right')
entry_total_cost.grid(row=5, column=3)

#========================== Command buttons =============================================

Total_button = Button(f1, padx=16, pady=8, font=('arial', 20, 'bold'), text='Total', fg='black',
                        bd=16, bg='powder blue', width=6, command=TotalButton)
Total_button.grid(row=6, column=1)

Reset_button = Button(f1, padx=16, pady=8, font=('arial', 20, 'bold'), text='Reset', fg='black',
                        bd=16, bg='powder blue', width=6, command=reset)
Reset_button.grid(row=6, column=2)

exit_button = Button(f1, padx=16, pady=8, font=('arial', 20, 'bold'), text='EXIT', fg='black',
                        bd=16, bg='powder blue', width=6, command=qexit)
exit_button.grid(row=6, column=3)

root.mainloop()