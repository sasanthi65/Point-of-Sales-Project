from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def add():  # add function
    try:
        tot = 0
        item = item_var.get()
        price = int(price_var.get())
        qty = int(qty_var.get())
        tot = price * qty
    except Exception:  # warn user if string values are entered on price and quantity
        messagebox.showerror("Error", "Only digits are allowed")
    except Exception as e:
        messagebox.showerror("Error", e)
    else:
        list1 = [[item_var.get(), price_var.get(), qty_var.get(), tot]]  # insert the data to a list
        list1.sort(key=lambda x: x[1], reverse=True)  # sort data in the list
        for i, (item, price, qty, tot) in enumerate(list1, start=-1):  # iterate the list by order
            tree.insert("", "end", values=(item, price, qty, tot))  # insert data in the list to the TreeView


    item_entry.delete(0, END)  # delete the data from the entries for the next data set
    price_entry.delete(0, END)
    qty_entry.delete(0, END)

    sum = 0  # define sum variable
    count = 0
    for child in tree.get_children():  # iterate the data in the TreeView
        sum += int(tree.item(child, 'values')[3])  # get the 3rd position value from the TreeView and add it to the sum
        # count+= int(tree.item(child, 'values')[2])
    total.set(sum)  # set the entry with the sum
    count = len(tree.get_children())  # get the count of the no of items entered
    count_var.set(count)


def remove():  # remove items in the TreeView
    rem = tree.selection()[0]  # remove one item per selection
    cur_tot = int(total.get())  # get current total
    x = int(tree.item(rem, 'values')[3])  # get the total of the selected item
    new_tot = cur_tot - x  # deduct the selected total from current total
    total.set(new_tot)  # assign the new total to the total
    tree.delete(rem)  # remove the selected item
    count = int(count_var.get())
    new_count=count-1
    count_var.set(new_count)

def pay():  # pay function
    sub_tot = int(total.get())  # retrieve data of the total_entry through total variable
    pay = int(pay_var.get())
    balance = pay - sub_tot
    bal.set(balance)  # set the balance to the entry


def save():  # save function
    invoice = num_var.get()
    sub_total = total.get()
    date = date_var.get()
    file = open("bill.txt", "a")  # create a new file or open the existing file for appending data
    if invoice == "":  # check whether invoice number is empty
        messagebox.showerror("Invoice No Error", "Please enter an invoice number")
    elif sub_total == 0:  # check whether sub total is empty
        messagebox.showerror("Error", "Please calculate total first")
    elif date == "":
        messagebox.showerror("Date Error", "Please enter the date")
    else:
        file.write("Invoice No: " + invoice + '\n')  # write invoice number into the text file
        file.write("Date :" + date + '\n')  # write date into the text file
        file.write("Total:" + str(sub_total) + '\n')  # write sub to to the text file
        file.close()
        messagebox.showinfo("Save", "Data has been saved successfully")


def clear():
    num_entry.delete(0, END)
    date_entry.delete(0, END)
    item_entry.delete(0, END)
    price_entry.delete(0, END)
    qty_entry.delete(0, END)
    tot_entry.delete(0, END)
    total.set(0)
    bal_entry.delete(0, END)
    pay_entry.delete(0, END)
    for i in tree.get_children():
        tree.delete(i)


window2 = Tk()
window2.title("Invoice")
window2.geometry("1000x600")
window2.resizable(0, 0)  # cannot resize the default window size

# Create Labels
inv_label = Label(text="Invoice", font=("Arial", 30, "bold"), fg="white", bg='LightSkyBlue4')  # heading
inv_label.place(x=0, y=0, width=1000)

# invoice no
num_label = Label(text="Invoice Number", font=("Arial", 14))
num_label.place(x=10, y=65)
num_var = StringVar()
num_entry = Entry(textvariable=num_var, font=("Arial", 12))
num_entry.place(x=170, y=70, width=130)

# date
date_label = Label(text="Date", font=("Arial", 14))
date_label.place(x=350, y=65)
date_var = StringVar()
date_entry = Entry(textvariable=date_var, font=("Arial", 12))
date_entry.place(x=400, y=70, width=170)

# labels
item_label = Label(text="Item", font=("Arial", 10))
price_label = Label(text="Price", font=("Arial", 10))
qty_label = Label(text="Quantity", font=("Arial", 10))

# place labels
item_label.place(x=10, y=100)
price_label.place(x=150, y=100)
qty_label.place(x=260, y=100)

# Create variables for entries
item_var = StringVar()
price_var = IntVar()
qty_var = IntVar()

# create entries
item_entry = Entry(textvariable=item_var, width=11, font=20)
price_entry = Entry(textvariable=price_var, width=8, font=20)
qty_entry = Entry(textvariable=qty_var, width=9, font=20)

# place entries
item_entry.place(x=10, y=120, height=32)
price_entry.place(x=150, y=120, height=32)
qty_entry.place(x=260, y=120, height=32)

# Create Add button
add_button = Button(text="Add", font=("Arial", 13), width=10, bg='LemonChiffon3', command=add)
add_button.place(x=400, y=120)

# Create remove button
rem_button = Button(text="Remove Item", font=("Arial", 13), width=10, bg='LemonChiffon3', command=remove)
rem_button.place(x=520, y=120, width=130)

# treeview
cols = ('Item', 'Price', 'Qty', 'Total')  # column headings
tree = ttk.Treeview(window2, columns=cols, show='headings')

for col in cols:
    tree.heading(col, text=col)
    tree.grid(row=1, column=0, columnspan=2)
    tree.place(x=10, y=200)

# total
tot_label = Label(text='Sub Total', font=("Arial", 14))
tot_label.place(x=10, y=450)
total = IntVar()
tot_entry = Entry(textvariable=total, font=("Arial", 12), width=15)
tot_entry.place(x=120, y=450)


# cash paid
pay_label = Label(text='Cash Paid', font=("Arial", 14))
pay_label.place(x=10, y=480)
pay_var = IntVar()
pay_entry = Entry(textvariable=pay_var, font=("Arial", 12), width=15)
pay_entry.place(x=120, y=480)


# Balance
bal_label = Label(text='Balance', font=("Arial", 14))
bal_label.place(x=10, y=510)
bal = IntVar()
bal_entry = Entry(textvariable=bal, font=("Arial", 12), width=15)
bal_entry.place(x=120, y=510)


# No of items
no_item_label = Label(text="Number of items:")
no_item_label.place(x=400, y=450)
count_var = IntVar()
item_count_label = Label(textvariable=count_var)
item_count_label.place(x=500, y=450)

# Pay button
pay_button = Button(text='Pay', font=("Arial", 12), bg='DodgerBlue3', fg='white', command=pay)
pay_button.place(x=20, y=550, width=70)
# Save button
save_button = Button(text="Save", font=("Arial", 12), bg='LightBlue', command=save)
save_button.place(x=120, y=550, width=70)
# clear button
clear_button = Button(text="Clear", font=("Arial", 12), bg='DeepSkyBlue3', command=clear)
clear_button.place(x=220, y=550, width=70)
window2.mainloop()
