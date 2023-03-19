from tkinter import *
import sys
import os
from tkinter import messagebox


def login():  # login button command
    if os.path.exists('./userlogin.txt'):  # check whether the text file is created in the current directory
        with open("userlogin.txt") as f:  # open created text file
            try:  # to handle errors
                new = f.readlines()  # read lines
                name = new[0].rstrip()  # assign the first line in text file to name variable
                password = new[1].rstrip()  # assign the first line in text file to password variable
                if username_entry.get() == name and password_entry.get() == password:  # check if the entered password and username match
                    messagebox.showinfo("Login", "Login Successful")  # show successful message
                    window.destroy()  # close the window
                    import invoice  # import invoice.py file
                elif username_entry.get()=="" or password_entry.get()=="":
                    messagebox.showerror("Error","Please enter all the details")
                else:
                    messagebox.showerror("Login Failed",
                                         "Username or Password is incorrect")  # show error message if incorrect password or username is entered
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)
            except Exception as e:  # if an error is found notify the user
                messagebox.showerror('Generic error:', str(e))
        f.close()
    else:  # if the file does not exists display the error
        messagebox.showerror("Error", "The data file is missing")


def cancel():  # cancel button
    sure = messagebox.askyesno("Cancel", "Are you sure you want to cancel?", parent=window)  # confirming twice
    if sure == True:
        window.destroy()  # if yes is chosen then close the window
        sys.exit()  # close the system


window = Tk()
window.title("Login")
window.geometry("500x350")
window.resizable(0, 0)  # cannot resize the default window size

# background
label = Label(window)
label.place(relx=0, rely=0, width=1200, height=800)
img = PhotoImage(file="images/Hm1A4K.png")
label.configure(image=img)

# Heading - Point of Sales System
label2 = Label(text="Point of Sales System", font=("Arial", 30, "bold"), bg='blue', fg='white')
label2.place(x=25, y=10, height=50, width=450)

# Create abels
username_label = Label(text="Username *", bg='bisque2', font=("Helvetica", 15))
password_label = Label(text="Password *", bg='dark goldenrod', font=("Helvetica", 15))
# place labels
username_label.place(x=40, y=120, width=140)
password_label.place(x=40, y=170, width=140)

# Create variables for entries
username = StringVar()  # define input type for variables
password = StringVar()

# Create entries or textboxes
username_entry = Entry(textvariable=username, width=20, bg='LightSteelBlue2',
                       font=("Helvetica", 15))  # assign variables
password_entry = Entry(textvariable=password, show='*', width=20, bg='LightSteelBlue2', font=("Helvetica", 15))
# place entries
username_entry.place(x=200, y=120, height=29)
password_entry.place(x=200, y=170, height=29)

# Create button
login_button = Button(text="Login", bg="teal", fg="white", width="15", height="1", font=("Arial", 15), command=login)
cancel_button = Button(text="Cancel", bg="grey", fg="black", width="15", height="1", font=("Arial", 15), command=cancel)
# place buuton
login_button.place(x=45, y=250)
cancel_button.place(x=250, y=250)

window.mainloop()
