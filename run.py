# coding=utf-8
import games
import heuristics
import start_rules

# game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()
state = game.initial

print "Nueva partida del Conecta-4.\n" \
      "La dificultad se puede escoger del 1 a 3, siendo 1 el nivel más fácil.\n"

level = start_rules.ask_difficulty()
player = start_rules.ask_who_starts()


def restart(decision):
    while decision != "n" and decision != "s":
        decision = raw_input()
    else:
        if decision == "s":
            game = games.ConnectFour()
            state = game.initial
            level = start_rules.ask_difficulty()
            player = start_rules.ask_who_starts()
        else:
            break


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        # move = games.minimax_decision(state, game)
        # move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, d=level, eval_fn=heuristics.get_move)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "\n\nFinal de la partida"
        decision = raw_input("¿Desea reiniciarla? (S/N)")

        restart(decision.lower())
