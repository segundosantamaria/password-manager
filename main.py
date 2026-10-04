from tkinter import Tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




def generate_pw():
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)
  letter2= [random.choice(letters) for char in range(nr_letters)]

  symb2=[random.choice(symbols) for char in range(nr_symbols)]

  num2=[random.choice(numbers) for char in range(nr_numbers)]

  password_list = letter2 + num2 + symb2

  random.shuffle(password_list)

  

  password = "".join(password_list)
  
  pw_entry.delete(0,END)
  pw_entry.insert(0, password)
  pyperclip.copy(password)
  

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    webget = web_entry.get()
    pwget = pw_entry.get()
    emailget = email_entry.get()
    
    
    if webget == "" or pwget == "" or emailget == "":
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")   
    else: 
        conf = messagebox.askokcancel(title=webget, message=f"These are the details entered: \nEmail:{emailget}"f"\nPassword: {pwget} \nIs it ok to save?")
        if conf:
            with open(r"Day 16-100\Day 29\data.txt", mode="a") as data:
                data.write(f"{webget} | {emailget} | {pwget} \n")
                web_entry.delete(0, END)
                pw_entry.delete(0, END)    

# ---------------------------- UI SETUP ------------------------------- #

window  = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)


canvas = Canvas(height=200, width=200)
img = PhotoImage(file=r"Day 16-100\Day 29\logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website = Label(text="Website:")
website.grid(row=1,column=0)
web_entry = Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2,sticky="EW")

email = Label(text="Email/Username:")
email.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="EW")


pw = Label(text="Password:")
pw.grid(row=3,column=0)
pw_entry = Entry(width=21)
pw_entry.grid(row=3,column=1,sticky="EW",padx=0)

generate_button = ttk.Button(text="Generate Password", command=generate_pw)
generate_button.grid(row=3,column=2)

add_button = ttk.Button(text="Add",width=36, command=save_pw)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()