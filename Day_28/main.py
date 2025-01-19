from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    check_lable.config(text="")
    timer_lable.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps%8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_lable.config(text="Break", fg=RED)
    elif reps%2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_lable.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    display_minutes = math.floor(count/60)
    distplay_seconds = count%60

    if display_minutes < 10:
        display_minutes = f"0{display_minutes}"

    if distplay_seconds < 10:
        distplay_seconds = f"0{distplay_seconds}"
    
    canvas.itemconfig(timer_text, text = f"{display_minutes}:{distplay_seconds}")
    
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "✓"
        check_lable.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Python\100_days_of_code\Day_28\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=2, row=2)

timer_lable = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer_lable.grid(column=2, row=1)

check_lable = Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check_lable.grid(column=2, row=4)

start_button = Button(text="Start", command=start_timer) 
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer) 
reset_button.grid(column=3, row=3)




window.mainloop()