from blockchain import Blockchain
from item_sharing import Owner, Item, Customer
from tkinter import *
#import tkMessageBox
import tkinter.messagebox as messagebox 


def show_balance(cust_balance, owner_balance):
    x="Customer balance: %s" % (cust_balance,)
    y="Owner balance: %s" % (owner_balance,)
    print(x)
    print(y)
    return x,y

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start(custbal):
    global x,y,total
    blockchain = Blockchain()
    customer = Customer(custbal)
    ownerbal = 500
    owner = Owner(ownerbal)
    eth = 50

    show_balance(customer.balance, owner.balance)

    #1
    owner.deploy(eth, blockchain)

    #2
    customer.request_book(eth, blockchain)

    #3
    item = "xyz"
    days_no = 1
    owner.add_item_to_rent(total, item)
    customer.pass_number_of_days(days_no)

    #4
    owner.encrypt_and_store_details(blockchain)
    owner.allow_item_usage()

    #5
    customer.access_item()

    #6
    customer.end_item_rental()

    #7
    owner.withdraw_earnings()
    customer.retrieve_balance()

    show_rental_cost(total)
    x,y=show_balance(customer.balance, owner.balance)
    


if __name__ == '__main__':
    custbal=1000
    x,y=0,0
    
        # import tkinter module


    # make a window
    window = Tk()

    # specify it's size
    window.geometry("700x600")

    # take a image for background
    # bg = PhotoImage(file='bg.png')

    # label it in the background
    # label17 = Label(window, image=bg)

    # position the image as well
    # label17.place(x=0, y=0)

    total=0
    # function to calculate the
    # price of all the orders
    def calculate():
        global total
            # dic for storing the
        # food quantity and price
        dic = {' Mysore_Masala_Dosa': [e1, 80],
            'Idli': [e2, 50],
            'Bisi_Bele_Bath': [e3, 100],
            'Upma': [e4, 50],
            'Filter_Coffee': [e5, 10],
            'Gulab_Jamun': [e6, 35]}
        total = 0
        for key, val in dic.items():
            if val[0].get() != "":
                total += int(val[0].get())*val[1]

        label16 = Label(window,
                        text="Your Total Bill is - "+str(total),
                        font="times 18")

        # position it
        label16.place(x=20, y=490)
        label16.after(1000, label16.destroy)
        window.after(1000, calculate)


    label8 = Label(window,
                text="Pai Tiffins Online Ordering",
                font="times 28 bold")
    label8.place(x=350, y=20, anchor="center")


    label1 = Label(window,
                text="Menu",
                font="times 28 bold")

    label1.place(x=520, y=70)

    label2 = Label(window, text="Mysore Masala Dosa \
    Rs 80", font="times 18")

    label2.place(x=450, y=120)

    label3 = Label(window, text="Idli \
    Rs 50", font="times 18")

    label3.place(x=450, y=150)

    label4 = Label(window, text="Bisi Bele Bath	 \
    Rs 100", font="times 18")
    label4.place(x=450, y=180)

    label5 = Label(window, text=" Upma \
    Rs 50", font="times 18")

    label5.place(x=450, y=210)

    label6 = Label(window, text="Filter Coffee\
    Rs 10", font="times 18")

    label6.place(x=450, y=240)

    label7 = Label(window, text="Gulab Jamun \
    Rs 35", font="times 18")

    label7.place(x=450, y=270)

    # billing section
    label9 = Label(window, text="Select the items",
                font="times 18")
    label9.place(x=115, y=70)

    label10 = Label(window,
                    text="Mysore Masala Dosa",
                    font="times 18")
    label10.place(x=20, y=120)

    e1 = Entry(window)
    e1.place(x=20, y=150)

    label11 = Label(window, text="Idli",
                    font="times 18")
    label11.place(x=20, y=200)

    e2 = Entry(window)
    e2.place(x=20, y=230)

    label12 = Label(window, text="Bisi Bele Bath",
                    font="times 18")
    label12.place(x=20, y=280)

    e3 = Entry(window)
    e3.place(x=20, y=310)

    label13 = Label(window,
                    text="Upma",
                    font="times 18")
    label13.place(x=20, y=360)

    e4 = Entry(window)
    e4.place(x=20, y=390)

    label14 = Label(window,
                    text="Filter Coffee",
                    font="times 18")
    label14.place(x=250, y=120)

    e5 = Entry(window)
    e5.place(x=250, y=150)

    label15 = Label(window,
                    text="Gulab Jamun",
                    font="times 18")

    label15.place(x=250, y=200)


    
    def helloCallBack():
        global total,x
        messagebox.showinfo( message="Total Bill: "+str(total)+"     \n"+"Wallet Balance: "+str(1000-total))


    B = Button(window, text ="Submit", command = helloCallBack)
    B.place(x=250,y=460,width=80)

    e6 = Entry(window)
    e6.place(x=250, y=230)
    
    # execute calculate function after 1 second
    window.after(1000, calculate)
    
    # closing the main loop
    window.mainloop()
    start(custbal)

