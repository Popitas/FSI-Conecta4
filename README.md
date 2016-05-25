# Conecta 4

En este programa, se plantea una forma de juego en el que un usuario es
capaz de enfrentarse a la máquina. Se ha incorporado una heurística que
aporta cierto sentido de victoria o derrota al computador.

En primer lugar, se da más relevancia a los movimientos que terminan la
partida. Se valora más los movimientos en los que la máquina gana.

En caso de no ser un movimiento ganador, se evaluarán los posibles
movimientos, puntuando positivamente los que benefician a la máquina y
penalizando los que favorecen al usuario.

Además, se ponderan los movimientos atendiendo al número de fichas 
consecutivas y a su posición absoluta en el tablero -las columnas
centrales añaden más valor, ya que permiten un mayor número de posibles
movimientos ganadores-.