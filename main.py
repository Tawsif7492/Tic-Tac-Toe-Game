import random
import tkinter as tk


def n_game():
    x = new_game.cget("text")
    y = new_game.cget("text")
    if y == "New Game":
        z = random.randint(0, 10)
        if z < 5:
            text.config(text="Player1's Turn")
        elif z > 5:
            text.config(text="Player2's Turn")
    if x == "Start Game":
        new_game.config(text="New Game")
        z = random.randint(0, 10)
        if z < 5:
            text.config(text="Player1's Turn")
        elif z > 5:
            text.config(text="Player2's Turn")
    for button in btn_list:
        if button.cget("text"):
            button.config(text="")
        button.config(state="normal")

i = [0]
j = [0]

def turn(btn):
    if n_game:
        turn = text.cget("text")
        clicked = btn.cget("text")
        if turn == "Player1's Turn" and clicked == "":
            btn.config(text="X")
            text.config(text="Player2's Turn")
        elif turn == "Player2's Turn" and clicked == "":
            btn.config(text="O")
            text.config(text="Player1's Turn")
    x0, x1, x2, x3, x4, x5, x6, x7, x8 = btn0.cget("text"), btn1.cget(
        "text"), btn2.cget("text"), btn3.cget("text"), btn4.cget(
            "text"), btn5.cget("text"), btn6.cget("text"), btn7.cget(
                "text"), btn8.cget("text")
    if x0 == "X" and x1 == "X" and x2 == "X" or x0 == "X" and x3 == "X" and x6 == "X" or x0 == "X" and x4 == "X" and x8 == "X" or x1 == "X" and x4 == "X" and x7 == "X" or x2 == "X" and x5 == "X" and x8 == "X" or x2 == "X" and x4 == "X" and x6 == "X" or x6 == "X" and x7 == "X" and x8 == "X" or x3 == "X" and x4 == "X" and x5 == "X":
        text.config(text="Player1 Won")
        i[0] += 1
        p_win.config(text=i[0])
    elif x0 == "O" and x1 == "O" and x2 == "O" or x0 == "O" and x3 == "O" and x6 == "O" or x0 == "O" and x4 == "O" and x8 == "O" or x1 == "O" and x4 == "O" and x7 == "O" or x2 == "O" and x5 == "O" and x8 == "O" or x2 == "O" and x4 == "O" and x6 == "O" or x6 == "O" and x7 == "O" and x8 == "O" or x3 == "O" and x4 == "O" and x5 == "O":
        text.config(text="Player2 Won")
        j[0] += 1
        c_win.config(text=j[0])
    elif x0 != "" and x1 != "" and x2 != "" and x3 != "" and x4 != "" and x5 != "" and x6 != "" and x7 != "" and x8 != "":
        text.config(text="It's a Draw")


root = tk.Tk()
root.attributes("-fullscreen", True)

player = tk.Label(root,
                  text="Player1(X)",
                  font="Default, 18",
                  padx="90",
                  pady="35")
player.grid(row=0, column=0)
p_win = tk.Label(root, text=0, font="Default, 18")
p_win.grid(row=1, column=0)

computer = tk.Label(root, text="Player2(O)", font="Default, 18", padx="90")
computer.grid(row=0, column=2)
c_win = tk.Label(root, text=0, font="Default, 18")
c_win.grid(row=1, column=2)

text = tk.Label(root, text="Please start the game", font="Default, 18")
text.grid(row=0, column=1)

button_frame = tk.Frame(root, pady="30")
button_frame.grid(row=2, column=1)

new_game = tk.Button(button_frame,
                     text="Start Game",
                     font="Default, 18",
                     command=n_game)
new_game.pack()

game_frame = tk.Frame(root)
game_frame.grid(row=1, column=1)

btn0 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn0))
btn1 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn1))
btn2 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn2))
btn3 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn3))
btn4 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn4))
btn5 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn5))
btn6 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn6))
btn7 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn7))
btn8 = tk.Button(game_frame,
                 text="",
                 height="1",
                 width="2",
                 font="Default, 38",
                 compound="center",
                 state="disabled",
                 command=lambda: turn(btn8))

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=1, column=2)
btn6.grid(row=2, column=0)
btn7.grid(row=2, column=1)
btn8.grid(row=2, column=2)

btn_list = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8]


root.mainloop()
