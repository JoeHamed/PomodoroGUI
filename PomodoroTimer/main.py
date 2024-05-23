from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFEF78"
VIOLET = "#7027A0"
TEAL = "#1DB9C3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", fg=TEAL)
    global marks, reps
    marks = ""
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        time_label.config(text="Break", fg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        time_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        time_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=VIOLET)

time_label = Label(text="Timer", fg=TEAL, font=(FONT_NAME, 30, "bold"), bg=VIOLET)
time_label.grid(column=1, row=0)

check_mark = Label(fg=TEAL, bg=VIOLET, font=(FONT_NAME, 10, "bold"))
check_mark.config(pady=5)
check_mark.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=VIOLET, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
