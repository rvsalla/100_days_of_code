from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    km_result_lable.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_lable = Label(text="Miles")
miles_lable.grid(column=2, row=0)

equals_lable = Label(text="is equals to")
equals_lable.grid(column=0, row=1)

km_result_lable = Label(text="0")
km_result_lable.grid(column=1, row=1)

km_lable = Label(text="Km")
km_lable.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km) 
calculate_button.grid(column=1, row=2)

window.mainloop()