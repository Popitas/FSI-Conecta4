# coding=utf-8
def ask_difficulty():
    level = 0
    while level not in range(1, 6):
        level = input("Seleccione el nivel de dificultad (1-5): ")

    return level


def ask_who_starts():
    while True:
        first_player = raw_input("¿Quiere que empiece la máquina? (S/N): ")
        if first_player.lower() in ['s', 'n']:
            if first_player.lower() == 's':
                return 'X'
            else:
                return 'O'
