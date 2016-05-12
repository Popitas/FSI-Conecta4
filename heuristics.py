def get_move_value(state, game):
    if state.utility == -1:
        return state.utility * 1000000 + contarfichas(state, game)
    elif state.utility == 1:
        return state.utility * 1000000 - contarfichas(state, game)
    else:
        valor = 0
        for x in range(1, game.h + 1):
            for y in range(1, game.v + 1):
                if state.board.get((x, y)) == "X":
                    valor += compute_utility(state.board, (x, y), "X")
                elif state.board.get((x, y)) == "0":
                    valor -= compute_utility(state.board, (x, y), "O")

    return valor


def compute_utility(board, move, player):
    return k_in_row(board, move, player, (0, 1)) + \
           k_in_row(board, move, player, (1, 0)) + \
           k_in_row(board, move, player, (1, -1)) + \
           k_in_row(board, move, player, (1, 1))


def k_in_row(board, move, player, (delta_x, delta_y)):
    x, y = move
    n = 0
    acumulado = 0
    while board.get((x, y)) == player:
        n += 1
        acumulado += sumacolumna(x)
        x, y = x + delta_x, y + delta_y

    x, y = move
    while board.get((x, y)) == player:
        n += 1
        acumulado += sumacolumna(x)
        x, y = x - delta_x, y - delta_y

    n -= 1  # Because we counted move itself twice
    return n * acumulado


def sumacolumna(columna):
    if columna == 4:
        return 300
    elif columna == 3 or columna == 5:
        return 200
    else:
        return 100


def contarfichas(state, game):
    contador = 0
    for x in range(1, game.h + 1):
        for y in range(1, game.v + 1):
            if state.board.get((x, y)) == "X":
                contador += 1
    return contador
