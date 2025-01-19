# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #window = Tk()
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file=r"C:\Python\100_days_of_code\Day_29\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

website_lable = Label(text="Website:")
website_lable.grid(column=1, row=2)

email_lable = Label(text="Email/Username:")
email_lable.grid(column=1, row=3)

password_lable = Label(text="Password:", width=21)
password_lable.grid(column=1, row=4)

website_entry = Entry(width=35)
print(website_entry.get())
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
print(email_entry.get())
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(END, "example@email.com")

password_entry = Entry(width=21)
print(password_entry.get())
password_entry.grid(column=2, row=4)

generate_button = Button(text="Generate Password", width=21) 
generate_button.grid(column=3, row=4)

add_button = Button(text="ReAddset", width=36) 
add_button.grid(column=2, row=5, columnspan=2)





window.mainloop()