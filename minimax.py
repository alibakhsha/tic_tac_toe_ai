import time
from game import AI, HUMAN

nodes_visited = 0

def minimax(game, depth, is_maximizing):
    global nodes_visited
    nodes_visited += 1

    if game.is_terminal():
        return game.evaluate(), None

    if is_maximizing:
        best_score = -float('inf')
        best_move = None

        for move in game.available_moves():
            game.make_move(*move, AI)
            score, _ = minimax(game, depth + 1, False)
            game.undo_move(*move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    else:
        best_score = float('inf')
        best_move = None

        for move in game.available_moves():
            game.make_move(*move, HUMAN)
            score, _ = minimax(game, depth + 1, True)
            game.undo_move(*move)

            if score < best_score:
                best_score = score
                best_move = move

        return best_score, best_move
