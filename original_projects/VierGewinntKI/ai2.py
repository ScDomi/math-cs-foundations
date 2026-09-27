from helper import *
import copy
import math
import time

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


    def scoring_position(board, player):            # evaluate current board posotion by summing up the value of all possible
        score = 0                                   # windows of four connected fields

        # center 
        center_arr = [board[row][N_COLS//2] for row in range(N_ROWS)]
        center_count = center_arr.count(player)
        score += center_count * 3
        # horizontal
        for row in range(N_ROWS):
            row_arr = [int(i) for i in list(board[row])]
            for col in range(N_COLS-3):
                check_four = row_arr[col:col+4]  # going through every possible horizontal four in a row
                score += eval_check_four(check_four, player)
        # vertical
        for col in range(N_COLS):
            col_arr = [int(i[col]) for i in list(board)]
            for row in range(N_ROWS-3):
                check_four = col_arr[row:row+4] # going through every possible vertical four in a column
                score += eval_check_four(check_four, player)
        # diagonal right up
        for row in range(N_ROWS-3):
            for col in range(N_COLS-3):
                check_four = [board[row+i][col+i] for i in range(N_COLS-3)] # going through every possible positive sloped diagonal
                score += eval_check_four(check_four, player)
        # diagonal right down
        for row in range(N_ROWS-3):
            for col in range(N_COLS-3):
                check_four = [board[row+3-i][col+i] for i in range(N_COLS-3)] # going through every possible negative sloped diagonal
                score += eval_check_four(check_four, player)
        return score

    def is_terminal_node(board):            # checking if the game is over, so no more child nodes are created in minimax
        if is_victory(board) == PLAYER_1 or is_victory(board) == PLAYER_2 or len(get_valid_locations(board)) == 0:
            return True
        return False

    def minimax(board, depth, alpha, beta, maximizing_player):      # looking into future moves
        valid_locations = get_valid_locations(board)
        if player == PLAYER_1:      
            opponent = PLAYER_2
        elif player == PLAYER_2:
            opponent = PLAYER_1

        if depth == 0 or is_terminal_node(board):    # at terminal node or Game End 
            if is_terminal_node(board):
                if is_victory(board) == player:         # rating position if ai wins
                    return (None, math.inf)
                elif is_victory(board) == opponent:     # rating position if opponent wins
                    return (None, -math.inf)
                else:                                   # Game over
                    return (None, 0)
            else:   # Depth equal to 0
                return (None, scoring_position(board, player))
        
        if maximizing_player:
            value = -math.inf
            best_column = random.choice(valid_locations)
            for col in valid_locations:
                temp_board = copy.deepcopy(board)
                place_token(arr=temp_board, col=col, player=player)
                new_score = minimax(temp_board, depth-1, alpha, beta, False)[1]     # next player is minimizing player
                if new_score > value:                                               # only move with best rating (best for ai) 
                    value = new_score                                               # is saved
                    best_column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return (best_column, value)
        else:   # minimizing player (in this case opponent)
            value = math.inf
            best_column = random.choice(valid_locations)
            for col in valid_locations:
                temp_board = copy.deepcopy(board)
                place_token(temp_board, col, opponent)
                new_score = minimax(temp_board, depth-1, alpha, beta, True)[1]      # next player is maximizing player
                if new_score < value:                                               # only move with worst rating (best for opponent)
                    value = new_score                                               # is saved
                    best_column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return (best_column, value)

    

    def eval_check_four(check_four, player):        # evaluate score of four connected fields on board
        score = 0                                   # by counting own/opponents pieces and empty fields                        
        if player == PLAYER_1:                      
            opponent = PLAYER_2
        else:
            opponent = PLAYER_1

        # the weight of these cases / the impact of each case on the score can be changed
        if check_four.count(player) == 4:           # not important because minimax, but doesnt matter
            score += 100                            
        elif check_four.count(player) == 3 and check_four.count(0) == 1:
            score += 5
        elif check_four.count(player) == 2 and check_four.count(0) == 2:
            score += 2

        if check_four.count(opponent) == 3 and check_four.count(0) == 1:
            score -= 4
        return score
        
    
    def get_valid_locations(board):                 # to make sure, ai is making no invalid moves
        valid_locations = []
        for col in range(N_COLS):
            if not column_is_full(board, col):
                valid_locations.append(col)

        return valid_locations
    

    return minimax(arr, 5, -math.inf, math.inf, True)[0]

########## This function can also be used for the minimax function, but isnt optimized with Alpha-Beta-Pruning ##########

    # def minimax(board, depth, maximizing_player):
    #     valid_locations = get_valid_locations(board)
    #     if player == PLAYER_1:      
    #         opponent = PLAYER_2
    #     elif player == PLAYER_2:
    #         opponent = PLAYER_1

    #     if depth == 0 or is_terminal_node(board):
    #         if is_terminal_node(board):
    #             if is_victory(board) == player:
    #                 return (None, 1000000000)
    #             elif is_victory(board) == opponent:
    #                 return (None, -100000000)
    #             else:                   # Some wierd case, Game over
    #                 return (None, 0)
    #         else:   # Depth equal to 0
    #             return (None, scoring_position(board, player))
        
    #     if maximizing_player:
    #         value = -math.inf
    #         best_column = random.choice(valid_locations)
            
    #         for col in valid_locations:
    #             temp_board = copy.deepcopy(board)
    #             current_score = scoring_position(temp_board, player)
    #             place_token(arr=temp_board, col=col, player=player)
    #             new_score = minimax(temp_board, depth-1, False)[1]
    #             if new_score > value:
    #                 value = new_score
    #                 best_column = col
                
    #         return (best_column, value)
    #     else:   # minimizing player
    #         value = math.inf
    #         best_column = random.choice(valid_locations)
            
    #         for col in valid_locations:
    #             temp_board = copy.deepcopy(board)
    #             place_token(temp_board, col, opponent)
    #             new_score = minimax(temp_board, depth-1, True)[1] 
    #             if new_score < value:
    #                 value = new_score
    #                 best_column = col
                
    #         return (best_column, value)
    # return minimax(arr, 1, True)[0]    


##### without alpha beta pruning ######

    # def scoring_position(board, player):
    #     score = 0

    #     # center 
    #     center_arr = [board[row][N_COLS//2] for row in range(N_ROWS)]
    #     center_count = center_arr.count(player)
    #     score += center_count * 3
    #     # horizontal
    #     for row in range(N_ROWS):
    #         row_arr = [int(i) for i in list(board[row])]
    #         for col in range(N_COLS-3):
    #             check_four = row_arr[col:col+4]  # going through every possible horizontal four in a row
    #             score += eval_check_four(check_four, player)
    #     # vertical
    #     for col in range(N_COLS):
    #         col_arr = [int(i[col]) for i in list(board)]
    #         for row in range(N_ROWS-3):
    #             check_four = col_arr[row:row+4] # going through every possible vertical four in a column
    #             score += eval_check_four(check_four, player)
    #     # diagonal right up
    #     for row in range(N_ROWS-3):
    #         for col in range(N_COLS-3):
    #             check_four = [board[row+i][col+i] for i in range(N_COLS-3)] # going through every possible positive sloped diagonal
    #             score += eval_check_four(check_four, player)
    #     # diagonal right down
    #     for row in range(N_ROWS-3):
    #         for col in range(N_COLS-3):
    #             check_four = [board[row+3-i][col+i] for i in range(N_COLS-3)] # going through every possible negative sloped diagonal
    #             score += eval_check_four(check_four, player)
    #     return score

    # def is_terminal_node(board):            # checking if the game is over, so no child nodes are created in minimax
    #     if is_victory(board) == PLAYER_1 or is_victory(board) == PLAYER_2 or len(get_valid_locations(board)) == 0:
    #         return True
    #     return False

    # def minimax(board, depth, maximizing_player):
    #     valid_locations = get_valid_locations(board)
    #     if player == PLAYER_1:      
    #         opponent = PLAYER_2
    #     elif player == PLAYER_2:
    #         opponent = PLAYER_1

    #     if depth == 0 or is_terminal_node(board):
    #         if is_terminal_node(board):
    #             if is_victory(board) == player:
    #                 return (None, 1000000000)
    #             elif is_victory(board) == opponent:
    #                 return (None, -100000000)
    #             else:                   # Some wierd case, Game over
    #                 return (None, 0)
    #         else:   # Depth equal to 0
    #             return (None, scoring_position(board, player))
        
    #     if maximizing_player:
    #         value = -math.inf
    #         best_column = random.choice(valid_locations)
    #         for col in valid_locations:
    #             temp_board = copy.deepcopy(board)
    #             place_token(arr=temp_board, col=col, player=player)
    #             new_score = minimax(temp_board, depth-1, False)[1]
    #             if new_score > value:
    #                 value = new_score
    #                 best_column = col
    #         return (best_column, value)
    #     else:   # minimizing player
    #         value = math.inf
    #         best_column = random.choice(valid_locations)
    #         for col in valid_locations:
    #             temp_board = copy.deepcopy(board)
    #             place_token(temp_board, col, opponent)
    #             new_score = minimax(temp_board, depth-1, True)[1]
    #             if new_score < value:
    #                 value = new_score
    #                 best_column = col
    #         return (best_column, value)

    

    # def eval_check_four(check_four, player):        # evaluate score of four connected fields on board
    #     score = 0                                   # by counting own/opponents pieces                         
    #     if player == PLAYER_1:
    #         opponent = PLAYER_2
    #     else:
    #         opponent = PLAYER_2


    #     if check_four.count(player) == 4:           # not important if depth of minimax isnt equal to zero
    #         score += 100                            
    #     elif check_four.count(player) == 3 and check_four.count(0) == 1:
    #         score += 5
    #     elif check_four.count(player) == 2 and check_four.count(0) == 2:
    #         score += 2

    #     if check_four.count(opponent) == 3 and check_four.count(0) == 1:
    #         score -= 4
    #     return score
        
    

    # def get_valid_locations(board):
    #     valid_locations = []
    #     for col in range(N_COLS):
    #         if not column_is_full(board, col):
    #             valid_locations.append(col)

    #     return valid_locations

    # def pick_best_move(board, player):              # this function is not important for the final version of the ai
    #     best_score = -100000
    #     valid_locations = get_valid_locations(board)
    #     best_column = random.choice(valid_locations)
    #     for col in valid_locations:
    #         temp_board = copy.deepcopy(board)
    #         place_token(temp_board, col, player)
    #         score = scoring_position(temp_board, player)
    #         if score > best_score:
    #             best_score = score
    #             best_column = col
        
    #     return best_column

    # return minimax(arr, 3, True)[0]

    # def heuristic(game):
    #     rating = 0
    #     for column in range(7):
    #         for row in range(6):
    #             if column == 1 or column == 5:
    #                 if game[row][column] == 1:
    #                     rating += 1
    #                 elif game[row][column] == 2:
    #                     rating -= 1
                
    #             if column == 2 or column == 4:
    #                 if game[row][column] == 1:
    #                     rating += 2
    #                 elif game[row][column] == 2:
    #                     rating -= 2
                
    #             if column == 3:
    #                 if game[row][column] == 1:
    #                     rating += 3
    #                 elif game[row][column] == 2:
    #                     rating -= 3
    #     return rating


    # rating = (0, 0)

    # for column in range(7):
    #     game = copy.deepcopy(arr)
    #     place_token(game, column, player)
    #     if rating[0] < heuristic(game):
    #         rating = (heuristic(game), column)

    # return rating[1]
    
    # # randomly place tokens
    # while True:
    #     col = random.randint(0, N_COLS - 1)
    #     if not column_is_full(arr, col):
    #         return col

