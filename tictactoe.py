"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player by making random moves, 
    alternating between players. The function should return when the game is over. 
    The modified board will contain the state of the game, so the function does not return anything. 
    In other words, the function should modify the board input.
    """
    # get empty sqauares and loop until all sqaures are filled
    empty_squares = board.get_empty_squares()
    while (len(empty_squares) > 0):
        # check if game is over 
        if board.check_win() == None:
            # get a random element from the empty_square list and move the current player
            chosen_square = random.randrange(0, len(empty_squares))
            board.move(empty_squares[chosen_square][0], empty_squares[chosen_square][1], player)
            empty_squares = board.get_empty_squares()
            player = provided.switch_player(player)
        else:
            # empty the empty_sqaues list
            empty_squares = []
        
def mc_update_scores(scores, board, player):
    """
    A function that calculates the score based on who won and the player moves
    """
    # If the game is a tie then return the scores
    if board.check_win() == provided.DRAW:
        return scores
    else:
        # else loop through each grid and if current player won then icrement score else decrement score
        for row in range(0, board.get_dim()):
            for col in range(0, board.get_dim()):
                if board.square(row, col) == provided.EMPTY:
                    continue
                elif board.square(row, col) == player and player == board.check_win():
                    scores[row][col] = scores[row][col] + SCORE_CURRENT
                elif board.square(row, col) == player and player != board.check_win():
                    scores[row][col] = scores[row][col] - SCORE_CURRENT
                elif board.square(row, col) != player and player == board.check_win():
                    scores[row][col] = scores[row][col] - SCORE_OTHER
                elif board.square(row, col) != player and player != board.check_win():
                    scores[row][col] = scores[row][col] + SCORE_OTHER
        return scores

def get_best_move(board, scores):
    """
    From the scores grid decide the best move
    """
    #get the empty squares as a list
    empty_squares = board.get_empty_squares()
    possible_moves = []
    # loop through the empty squares and form a list that holds the scores
    # of those empty squares to decide a possible next move
    for square in empty_squares:
        possible_moves.append(scores[square[0]][square[1]])
    # get the max score
    max_score = max(possible_moves)
    possible_moves = []
    #filter out the squares where score is max
    for square in empty_squares:
        if scores[square[0]][square[1]] == max_score:
            possible_moves.append(square)
    # select a best move
    best_move = random.randrange(0, len(possible_moves))
    return possible_moves[best_move]

def mc_move(board, player, trials):
    """
    The main function that calls other helper functions
    to simulate a Monte Carlo trial to come up with the best move
    """
    # clone the board for passing it onto the helper functions
    
    # create the score grid
    scores = []
    
    for row in range(0, board.get_dim()):
        scores.append(row)
        score = []
        for col in range(0, board.get_dim()):
            col = 0
            score.append(col)
        scores[row] = score
    # simulate the monte carlo trials
    trial = 1
    while trial <= NTRIALS:
        # to simulate the trial moves
        trial_board = board.clone()
        mc_trial(trial_board, player)
        scores = mc_update_scores(scores, trial_board, player)
        trial += 1
    # return best move
    return get_best_move(board, scores)


#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
