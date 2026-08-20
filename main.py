import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

SPEED = 100  # Lower = faster

window = tk.Tk()
window.title(" Snake Game")
window.resizable(False, False)

score = 0
game_over = False
direction = "Right"
next_direction = "Right"

canvas = tk.Canvas(
    window,
    width=WIDTH,
    height=HEIGHT,
    bg="blue"
)
canvas.pack()

# Score display
score_label = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 16, "bold")
)
score_label.pack()

snake = [
    [100, 100],
    [80, 100],
    [60, 100]
]

def create_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)

        if [x, y] not in snake:
            return [x, y]


food = create_food()

def draw_game():
    canvas.delete("all")

    # Draw food
    x, y = food
    canvas.create_oval(
        x,
        y,
        x + CELL_SIZE,
        y + CELL_SIZE,
        fill="red"
    )


    for i, (x, y) in enumerate(snake):
        if i == 0:
        
            canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill="lime",
                outline="white"
            )
        else:
        
            canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill="green",
                outline="black"
            )


def change_direction(new_direction):

    global next_direction


    if new_direction == "Up" and direction != "Down":
        next_direction = "Up"

    elif new_direction == "Down" and direction != "Up":
        next_direction = "Down"

    elif new_direction == "Left" and direction != "Right":
        next_direction = "Left"

    elif new_direction == "Right" and direction != "Left":
        next_direction = "Right"



    global direction
    global food
    global score
    global game_over

    if game_over:
        return

    direction = next_direction


    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= CELL_SIZE

    elif direction == "Down":
        head_y += CELL_SIZE

    elif direction == "Left":
        head_x -= CELL_SIZE

    elif direction == "Right":
        head_x += CELL_SIZE

    new_head = [head_x, head_y]


    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        end_game()
        return


    if new_head in snake:
        end_game()
        return
    snake.insert(0, new_head)

    
    if new_head == food:

        score += 10
        score_label.config(text=f"Score: {score}")

        food = create_food()

    else:

        snake.pop()


    draw_game()


    window.after(SPEED, move_snake)


def end_game():

    global game_over

    game_over = True

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 - 20,
        text="GAME OVER",
        fill="red",
        font=("Arial", 35, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 30,
        text=f"Final Score: {score}",
        fill="white",
        font=("Arial", 20)
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 70,
        text="Press R to Restart",
        fill="yellow",
        font=("Arial", 16)
    )


def restart_game(event=None):

    global snake
    global food
    global score
    global game_over
    global direction
    global next_direction

    snake = [
        [100, 100],
        [80, 100],
        [60, 100]
    ]

    food = create_food()

    score = 0

    direction = "Right"
    next_direction = "Right"

    game_over = False

    score_label.config(text="Score: 0")

    draw_game()

    move_snake()



window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))
window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Right>", lambda event: change_direction("Right"))

window.bind("w", lambda event: change_direction("Up"))
window.bind("s", lambda event: change_direction("Down"))
window.bind("a", lambda event: change_direction("Left"))
window.bind("d", lambda event: change_direction("Right"))

window.bind("r", restart_game)
window.bind("R", restart_game)

draw_game()
move_snake()

window.mainloop()
