import time
from game import TicTacToe, HUMAN, AI
import minimax
import alphabeta

def print_board(board):
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell if cell else "-", end=" ")
        print("|")
    print()

def choose_algorithm():
    print("Choose Algorithm:")
    print("1 - Minimax")
    print("2 - Alpha-Beta Pruning")
    while True:
        choice = input("Enter choice (1 or 2): ")
        if choice in ("1", "2"):
            return choice

def main():
    game = TicTacToe()
    algo = choose_algorithm()

    print("\nYou are X, AI is O\n")

    while not game.is_terminal():
        print_board(game.board)

        # Human move
        while True:
            move = input("Enter your move (row col): ")
            try:
                r, c = map(int, move.split())
                if game.make_move(r, c, HUMAN):
                    break
                else:
                    print("Invalid move, try again.")
            except:
                print("Format: row col (e.g. 1 2)")

        if game.is_terminal():
            break

        # AI move
        print("\nAI thinking...\n")
        start = time.time()

        if algo == "1":
            minimax.nodes_visited = 0
            _, move = minimax.minimax(game, 0, True)
            nodes = minimax.nodes_visited
            name = "Minimax"
        else:
            alphabeta.nodes_visited = 0
            _, move = alphabeta.alphabeta(game, 0, -1, 1, True)
            nodes = alphabeta.nodes_visited
            name = "Alpha-Beta"

        elapsed = time.time() - start
        game.make_move(*move, AI)

        print(f"{name} selected move: {move}")
        print(f"Nodes visited: {nodes}")
        print(f"Time: {elapsed:.6f} sec\n")

    print_board(game.board)

    if game.is_winner(HUMAN):
        print("🎉 You Win!")
    elif game.is_winner(AI):
        print("🤖 AI Wins!")
    else:
        print("🤝 Draw!")

if __name__ == "__main__":
    main()
