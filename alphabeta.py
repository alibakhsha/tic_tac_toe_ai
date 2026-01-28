from game import AI, HUMAN

nodes_visited = 0

def alphabeta(game, depth, alpha, beta, is_maximizing):
    global nodes_visited
    nodes_visited += 1

    if game.is_terminal():
        return game.evaluate(), None

    if is_maximizing:
        best_move = None
        for move in game.available_moves():
            game.make_move(*move, AI)
            score, _ = alphabeta(game, depth + 1, alpha, beta, False)
            game.undo_move(*move)

            if score > alpha:
                alpha = score
                best_move = move

            if beta <= alpha:
                break  # PRUNING ✂️

        return alpha, best_move

    else:
        best_move = None
        for move in game.available_moves():
            game.make_move(*move, HUMAN)
            score, _ = alphabeta(game, depth + 1, alpha, beta, True)
            game.undo_move(*move)

            if score < beta:
                beta = score
                best_move = move

            if beta <= alpha:
                break  # PRUNING ✂️

        return beta, best_move
