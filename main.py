import tkinter as tk
import time
from game import TicTacToe, HUMAN, AI
import minimax
import alphabeta

USE_ALPHA_BETA = True  # برای مقایسه تغییر بده

game = TicTacToe()
root = tk.Tk()
root.title("Tic Tac Toe - AI")

buttons = [[None]*3 for _ in range(3)]
status = tk.Label(root, text="Your Turn", font=("Arial", 14))
status.grid(row=3, column=0, columnspan=3)

def on_click(r, c):
    if game.board[r][c] is not None or game.is_terminal():
        return

    game.make_move(r, c, HUMAN)
    buttons[r][c].config(text=HUMAN)

    if game.is_terminal():
        show_result()
        return

    ai_move()
    if game.is_terminal():
        show_result()

def ai_move():
    start = time.time()

    if USE_ALPHA_BETA:
        alphabeta.nodes_visited = 0
        _, move = alphabeta.alphabeta(game, 0, -1, 1, True)
        print("AlphaBeta Nodes:", alphabeta.nodes_visited)
    else:
        minimax.nodes_visited = 0
        _, move = minimax.minimax(game, 0, True)
        print("Minimax Nodes:", minimax.nodes_visited)

    print("Time:", time.time() - start)

    game.make_move(*move, AI)
    buttons[move[0]][move[1]].config(text=AI)

def show_result():
    if game.is_winner(HUMAN):
        status.config(text="You Win!")
    elif game.is_winner(AI):
        status.config(text="AI Wins!")
    else:
        status.config(text="Draw!")

for r in range(3):
    for c in range(3):
        btn = tk.Button(root, text="", font=("Arial", 24),
                        width=5, height=2,
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r, column=c)
        buttons[r][c] = btn

root.mainloop()
