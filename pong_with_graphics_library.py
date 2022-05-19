from graphics_lib import *

# Simple pong game - don't let the ball hit the bottom!
# KidsCanCode - Intro to Programming
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


def key_press(key):
    global paddle_speed
    if key == "Left":
        paddle_speed = -2
    elif key == "Right":
        paddle_speed = 2


# Animation loop
def draw_frame():
    global hit_bottom, bx, by, paddle_x, paddle_y, score, x_speed, y_speed
    if hit_bottom:
        x_speed = y_speed = 0
        draw_text(250, 200, text="GAME OVER", font=("Helvetica", 30))

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

    draw_oval(
        bx - ball_size, by - ball_size, bx + ball_size, by + ball_size, fill="red"
    )
    draw_rectangle(
        paddle_x,
        paddle_y,
        paddle_x + PADDLE_WIDTH,
        paddle_y + PADDLE_HEIGHT,
        fill="blue",
    )

    draw_text(5, 5, anchor=NW, text=f"Score: {score}")


start_graphics(draw_frame, window_title="Ball Game", key_press=key_press)
