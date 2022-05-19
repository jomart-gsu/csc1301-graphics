# Simple pong game - don't let the ball hit the bottom!
# Adapted from https://github.com/kidscancode/intro-python-code/blob/master/pong%20game.py
from tkinter import *
import random
import time

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

x_speed = random.randrange(-3, 3)
y_speed = -1
ball_size = 5
bx = 10
by = 10

paddle_x = 200
paddle_y = 300
paddle_speed = 0

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
score = 0

hit_bottom = False


def left_key_press(evt):
    global paddle_speed
    paddle_speed = -2


def key_press(evt):
    global paddle_speed
    if evt.keysym == "Left":
        paddle_speed = -2
    elif evt.keysym == "Right":
        paddle_speed = 2


# Create window and canvas to draw on
tk = Tk()
tk.title("Ball Game")
canvas = Canvas(tk, width=500, height=400, bd=0, bg="papaya whip")
canvas.pack()
canvas.bind_all("<KeyPress>", key_press)


# Animation loop
while hit_bottom == False:
    canvas.delete("all")

    paddle_x = min(max(0, paddle_x + paddle_speed), WINDOW_WIDTH - PADDLE_WIDTH)
    if bx <= ball_size or bx >= WINDOW_WIDTH - ball_size:
        x_speed = -x_speed
    if by <= ball_size:
        y_speed = -y_speed
    if (
        paddle_y - ball_size <= by <= paddle_y - ball_size + y_speed
        and paddle_x <= bx <= paddle_x + PADDLE_WIDTH
    ):
        score += 1
        if score % 2 == 0:
            y_speed *= 2

        y_speed = -y_speed
        x_speed = random.randrange(-3, 3)
    if by >= WINDOW_WIDTH:
        hit_bottom = True

    bx += x_speed
    by += y_speed

    canvas.create_oval(
        bx - ball_size, by - ball_size, bx + ball_size, by + ball_size, fill="red"
    )
    canvas.create_rectangle(
        paddle_x,
        paddle_y,
        paddle_x + PADDLE_WIDTH,
        paddle_y + PADDLE_HEIGHT,
        fill="blue",
    )

    label = canvas.create_text(5, 5, anchor=NW, text=f"Score: {score}")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# Game Over
canvas.create_text(250, 200, text="GAME OVER", font=("Helvetica", 30))
tk.update()
time.sleep(1)
