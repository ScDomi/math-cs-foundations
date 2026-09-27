from helper import *

#ai6

# Wie oft ist das Feld Teil einer möglichen 4er-Reihe?
feldBewertung = [[3, 4, 5, 7, 5, 4, 3],
                 [4, 6, 8, 10, 8, 6, 4],
                 [5, 8, 11, 13, 11, 8, 5],
                 [5, 8, 11, 13, 11, 8, 5],
                 [4, 6, 8, 10, 8, 6, 4],
                 [3, 4, 5, 7, 5, 4, 3]]

# KI: x-Koordinate
# Gegner: y-Koordinate
# es werden mögliche 4er Kombinationen durchgeschaut. Dabei wird pro Stein der
# Index von y oder x bei der Auswertung des Array erhöht. Befinden sich keine Gegnerischen
# Steine in der 4er-Feld-Kombination, dann wird ein wert zurückgeliefert. Andernfalls wird der Wert 0 zurückgegeben.
spielSituationBewertung = [[0, 10, 100, 1000, 10000],
                           [-10, 0, 0, 0],
                           [-100, 0, 0, 0],
                           [-1000, 0, 0, 0],
                           [-10000, 0, 0, 0]]

ai_player = 0
rival_player = 0


def ai(arr, player):
    """
    :param arr: current status of the board as type list[list[int]].
    The integers can either be 0 (cell empty), 1 (token of player 1) or 2 (token of player 2).
    :param player: Integer which is either 1 (turn of player 1) or 2 (turn of player 2).
    :return: Integer between 0 and 6 indicating in which row the next token shall be placed.

    Write your own AI in this function, do not change the function signature.
    Feel free to use any of the constants/methods in the helper.py / config.py file.
    You can/shall also override the ai() function in ai2.py to let
    different versions of you AI compete against each other.
    """

    # Variablen:
    global ai_player, rival_player
    ai_player = player
    rival_player = 1 if ai_player == 2 else 2

    # KI:
    return game_move(arr, player, 5)



######################## Min-Max-Algorithmus ##############################
# Gibt den Besten Spielzug zurück.
# Hohe Werte sind gut für die KI,
# niedrige Werte sind gut für den Gegenspieler
def game_move(arr, player, restTiefe):
    alpha_max = -100000000
    beta_min = 100000000
    best_column = -1

    # in jede Spalte einen Stein werfen
    for column in [3, 4, 2, 1, 5, 6, 0]:
        if not column_is_full(arr, column):
            arr, row = place_token2(arr, column, player)

            # Wenn der Mensch gewinnt, bekommen wir kleine Werte.
            # Wenn der Mensch nicht gewinnen kann, bekommen wir umso größere Werte,
            # weil der Mensch dann keine Punkte bekommt (da wir vll. gewinnen, oder den Zug klug gesetzt haben, um die
            # Gewinnmöglichkeit des Menschen zerstört haben.
            minWert = min(arr, change_player(player), alpha_max, beta_min, restTiefe)

            if minWert > alpha_max:
                best_column = column
                alpha_max = minWert

            # Zug rückgängig machen:
            arr[row][column] = 0

    # logging.debug("Bester Zugwert" + str(alpha_max))
    return best_column



def max(arr, player, alpha_max, beta_min, restTiefe):
    # gibt es durch den neu gesetzten Stein (in der vorherigen Methode) einen Gewinner?
    win_value = get_game_status_ai(arr, restTiefe)
    if win_value != GAME_NOT_FINISHED:
        return win_value

    # Falls kein Sieger nach "X" Zügen ermittelt werden konnte,
    # werden die aktuellen Züge bewertet
    if restTiefe == 0:
        return spielfeldBewertung(arr)

    # in jede Spalte einen Stein werfen
    for column in [3, 4, 2, 5, 1, 6, 0]:
        if not column_is_full(arr, column):
            arr, row = place_token2(arr, column, player)
            minWert = min(arr, change_player(player), alpha_max, beta_min, restTiefe - 1)

            if minWert > alpha_max:
                alpha_max = minWert

            # Zug rückgängig machen:
            arr[row][column] = 0

            # weil wir in der vorherigen Methode das Minimum suchen, können wir hier schon sagen,
            # falls das Minimum (Beta) übertroffen wurde, dass wir die Verarbeitung abbrechen,
            # weil der alpha_max-Wert ja nur ansteigen kann.
            if alpha_max >= beta_min:
                return beta_min

    return alpha_max


def min(arr, player, alpha_max, beta_min, restTiefe):
    # gibt es durch den neu gesetzten Stein (in der vorherigen Methode) einen Gewinner?
    win_value = get_game_status_ai(arr, restTiefe)
    if win_value != GAME_NOT_FINISHED:
        return win_value

    # Falls kein Sieger nach "X" Zügen ermittelt werden konnte,
    # werden die aktuellen Züge bewertet
    if restTiefe == 0:
        return spielfeldBewertung(arr)

    # in jede Spalte einen Stein werfen
    for column in [3, 4, 2, 5, 1, 6, 0]:

        if not column_is_full(arr, column):
            arr, row = place_token2(arr, column, player)
            maxWert = max(arr, change_player(player), alpha_max, beta_min, restTiefe - 1)

            if maxWert < beta_min:
                beta_min = maxWert

            # Zug rückgängig machen:
            arr[row][column] = 0

            # weil wir in der vorherigen Methode das Maximum suchen, können wir hier schon sagen,
            # falls das Maximum (Alpha) untertroffen wurde, dass wir die Verarbeitung abbrechen,
            # weil der beta_min-Wert ja nur abnehmen kann.
            if beta_min <= alpha_max:
                return alpha_max

    return beta_min




# Bewertet das Spielfeld, wenn in der untersten Baumebene noch kein Sieger festgestellt wurde
def spielfeldBewertung(arr):

    wert = 0
    if sum(x.count(0) for x in arr) < 28:
        wert = spielfeldBewertungAktuellerZug(arr)

    for row in range(N_ROWS):
        for column in range(N_COLS):
            if arr[row][column] == 0:
                continue
            if arr[row][column] == ai_player:
                # KI
                wert = wert + feldBewertung[row][column]
            else:
                # Gegenspieler
                wert = wert - feldBewertung[row][column]

    # logging.debug('WERT:' + str(wert))
    return wert * 2


# erweiterte Spielfeldbewertung, die die Gewinnmöglichkeiten anhand der noch möglichen Gewinnmöglichkeiten auswertet.
# siehe auch die Beschreibung zum Array "spielSituationBewertung" ganz oben in der Datei
def spielfeldBewertungAktuellerZug(arr):

    gesamtwert = 0

    # check if any player has four tokens in a row
    for c in range(N_COLS):
        for r in range(N_ROWS):
            wert1 = wert2 = wert3 = wert4 = 0

            # check for horizontal lines
            if c >= 3:
                list1 = [arr[r][c], arr[r][c - 1], arr[r][c - 2], arr[r][c - 3]]
                wert1 = spielSituationBewertung[list1.count(rival_player)][list1.count(ai_player)]

            # check for vertical lines
            # if r >= 3:
            #     list2 = [arr[r][c], arr[r - 1][c], arr[r - 2][c], arr[r - 3][c]]
            #     wert2 = spielSituationBewertung[list2.count(rival_player)][list2.count(ai_player)]

            # check for diagonal lines (type 1)
            if c >= 3 and r >= 3:
                list3 = [arr[r][c], arr[r - 1][c - 1], arr[r - 2][c - 2], arr[r - 3][c - 3]]
                wert3 = spielSituationBewertung[list3.count(rival_player)][list3.count(ai_player)]

            # check for diagonal lines (type 2)
            if c <= 3 and r >= 3:
                list4 = [arr[r][c], arr[r - 1][c + 1], arr[r - 2][c + 2], arr[r - 3][c + 3]]
                wert4 = spielSituationBewertung[list4.count(rival_player)][list4.count(ai_player)]

            gesamtwert += (wert1 + wert2 + wert3 + wert4)*(N_ROWS-r)

    #logging.debug('Aktuelle Bewertung: ' + str(gesamtwert))
    return gesamtwert




# ****************** Hilfsmethoden **********************
# wirft einen Stein in das Spielfeld
# gibt zusätzlich noch die Reihe zurück, um Performance zu sparren.
def place_token2(arr, col, player):
    # place token in lowermost position in the correct column
    row = -1
    for row in range(N_ROWS):
        if arr[row][col] == 0:
            arr[row][col] = player
            break

    output_board2(arr)
    return arr, row


def change_player(current_player):
    return PLAYER_2 if current_player == PLAYER_1 else PLAYER_1


# gibt einen Hohen Wert für den Min-Max Algorithmus zurück, wenn ein Spieler gewonnen hat.
# Dabei wird im Rückgabewert die aktuelle Resttiefe mit eingerechnet
# Es werden Positive Werte für die KI und negative Werte für den Gegner zurückgegeben
def get_game_status_ai(arr, current_deep):
    # beim letzten Durchlauf wäre die Resttiefe 0
    # und die Funktion würde keinen Gewinner zurückliefern
    current_deep += 1

    game_status = get_game_status(arr)
    if game_status == PLAYER_1_WINS:
        wert = 100000 if ai_player == PLAYER_1 else -100000
        # logging.debug('GEWINNWERT:' + str(wert * current_deep))
        return wert * current_deep
    elif game_status == PLAYER_2_WINS:
        wert = 100000 if ai_player == PLAYER_2 else -100000
        # logging.debug('GEWINNWERT:' + str(wert * current_deep))
        return wert * current_deep
    else:
        return game_status


# Ausgabe des Spielfelds, wenn der Min-Max-Algorithmus alle möglichen Kombinationen durchprobiert.
# -->Zum Debuggen:
def output_board2(arr):
    return
    # print board status in human-readable form
    logging.debug('xxxxxxxxxxxxxxxxxxxxxx')
    for row in range(N_ROWS - 1, -1, -1):
        string = GREY + '| '
        for col in range(N_COLS):
            if arr[row][col] == 0:
                string += '  '
            elif arr[row][col] == 1:
                string += 'X '
            elif arr[row][col] == 2:
                string += 'O '
            else:
                raise ValueError('Unknown value: ', arr[row][col])
        string += GREY + '| ' + str(row + 1)
        logging.debug(string)
    logging.debug('└ ─ ─ ─ ─ ─ ─ ─ ┘')
    logging.debug('  0 1 2 3 4 5 6  ')