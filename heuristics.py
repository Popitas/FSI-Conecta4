# coding=utf-8
from random import randint


def get_random_board_value(state):
    return randint(-100, 100)


def get_column_value(column):
    """Devuelve el valor asignado a una columna. Se da más importancia
    a las columnas centrales."""
    if column == 4:
        return 3
    elif column == (3 or 5):
        return 2
    else:
        return 1


def get_discs_in_line_value(board, move, player, (delta_x, delta_y)):
    """Asigna un valor a un movimiento que une fichas dándole más valor
    si se realiza en las columnas centrales."""
    x, y = move
    discs_in_row = 0
    line_value = 0
    while board.get((x, y)) == player:
        discs_in_row += 1
        line_value += get_column_value(x)
        x, y = x + delta_x, y + delta_y

    x, y = move
    while board.get((x, y)) == player:
        discs_in_row += 1
        line_value += get_column_value(x)
        x, y = x - delta_x, y - delta_y

    discs_in_row -= 1
    return discs_in_row * line_value


def get_move_value(board, move, player):
    """Devuelve el valor de un movimiento."""
    return get_discs_in_line_value(board, move, player, (0, 1)) + \
           get_discs_in_line_value(board, move, player, (1, 0)) + \
           get_discs_in_line_value(board, move, player, (1, -1)) + \
           get_discs_in_line_value(board, move, player, (1, 1))


def evaluate_moves(game, state):
    """Evalúa si un movimiento beneficia al jugador X (máquina)."""
    move_evaluation = 0

    for x in range(1, game.h):
        for y in range(1, game.v):
            if state.board.get(x, y) == 'X':
                move_evaluation += get_move_value(state.board, (x, y), 'X')
            if state.board.get(x, y) == 'O':
                move_evaluation -= get_move_value(state.board, (x, y), 'O')

    return move_evaluation


def get_board_value(state, game):
    """Devuelve el valor de una configuración del tablero. Se da más relevancia
    a los movimientos ganadores."""
    if state.utility == -1:
        return state.utility * 1000
    elif state.utility == 1:
        return state.utility * 2000
    else:
        return evaluate_moves(game, state)
