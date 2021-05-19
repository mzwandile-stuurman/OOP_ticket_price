# Mzwandile Stuurman

# Easy ticket
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Easy ticket calculator")
root.geometry("600x600")


class TicketSales:
    """options = ['Select category', 'Soccer', "Movie","Theatre"]
    variable = StringVar()
    variable.set(options[0])
    options_2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    variable2=StringVar()
    variable2.set(options_2[0])"""
    category= StringVar()
    tickets = StringVar()
    number= StringVar()
    amount = StringVar()
    category2= StringVar()
    tckets2=StringVar()
    ticktes2=StringVar()

    def __init__(self,master):
        # cell number label
        self.cell_label= Label(master, text="Enter Cell number")
        self.cell_label.place(x=10, y=50)
        self.cell_entry=Entry(master, textvariable=self.number)
        self.cell_entry.place(x=50, y=50)

        # category label and combobox
        self.category_label= Label(master, text="Select ticket category")
        self.category_label.place(x=10, y=100)
        self.category_menu=ttk.Combobox(master,textvariable=self.category)
        self.category_menu['values']= ('Movies','Soccer','Theatre')
        self.category_menu.current()
        self.category_menu.place(x=50,y=100)

        # ticket label and combobox
        self.price_label = Label(master, text="Number of tickets bought")
        self.price_label.place(x=10, y= 150)
        self.price_menu = ttk.Combobox(master)
        self.price_menu['values']= (1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        self.price_menu.current()
        self.price_menu.place(x=50,y=150)

        # calclulate button
        self.caclulate_btn= Button(master, text="Calculate Ticket" , command=self.CalcPrice)
        self.caclulate_btn.place(x=10, y=200)

        # exit button
        self.exit_btn = Button(master, text="Clear Entries")
        self.caclulate_btn.place(x= 50, y=200 )

        # amount label and entry
        self.amount_label = Label(master, text="Amount payable")
        self.amount_label.place(x=10, y=250)
        self.amount_entry = Entry(master, textvariable= self.amount)
        self.amount_entry.place(x=50,y=250)

        # number of tickets label and entry
        self.reservation = Label(master, text="Revervation for :")
        self.reservation.place(x=10, y=300)

        self.category_entry = Entry(master)
        self.category_entry.place(x=50,y=300)

        self.for_label = Label(master, text="for")
        self.for_label.place(x=75, y=300)

        self.number_entry = Entry(master)
        self.number_entry.place(x=100, y=300)

        # phone number display
        self.number_display_label=Label(master, text="Was done by")
        self.number_display_label.place(x=10,y= 350)

        self.number_display_entry = Entry(master)
        self.number_display_entry.place(x=50,y=350)





    def CalcPrice(self):
        category = self.category_menu.get()
        if category == 'Movies':
            price_movies = 75*int(self.price_menu.get()) + 0.14*75
            self.amount_entry.insert(0,price_movies)

        elif category== "Soccer":
            price_soccer= 40*float(self.price_menu.get()) + 0.14*40
            self.amount_entry.set(price_soccer)

        elif category == "Theatre":
            price_theatre = 100*float(self.price_menu.get()) + 0.14*100
            self.amount_entry.set(price_theatre)















x=TicketSales(root)
root.mainloop()




