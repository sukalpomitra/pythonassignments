"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
import random
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def gen_all_hold_combo(outcomes, length):
    """
    Iterative function that enumerates the set of all combinations of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length + 1):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)                
                if new_sequence.count(item) + 1 <= outcomes.count(item):
                    new_sequence.append(item)
                else:
                    continue
                temp_set.add(tuple(new_sequence))

            answer_set = answer_set.union(temp_set)
    #answer_set.remove(())
    return answer_set

def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def gen_sorted_hold_combo(outcomes, length):
    """
    Function that creates all sorted combinations via gen_all_sequences
    """    
    all_sequences = gen_all_hold_combo(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    #sort the hand
    current_hand = sorted(hand, reverse = True)
    max_score = 0
    score_streak  = 0
    previous_value = 0
    idx = 0
    # loop through current hand and get the sum of
    # same value die faces and then return the max 
    # them
    for value in current_hand:
        if len(current_hand) == 1:
            max_score = value
        elif previous_value == 0:
            score_streak = value
        elif previous_value == value:
            score_streak += value
            if idx + 1 == len(current_hand) and score_streak > max_score:
                max_score = score_streak
        else:
            if score_streak > max_score:
                max_score = score_streak
                
            if idx + 1 == len(current_hand) and value > max_score:
                max_score = value
            score_streak = value
        idx += 1
        previous_value = value

    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    dice_values = []
    # create the dice values from no of die sides
    for idx in range(1, num_die_sides + 1):
        dice_values.append(idx)
    # get the possible sequence list
    seq_list = gen_all_sequences(dice_values, num_free_dice)
    score_list = []
    # create a list of scores taht is generated through each seq
    # of die values
    for seq in seq_list:
        score_list.append(score(held_dice + tuple(seq)))
    # return the expected value
    return float(sum(score_list)) / len(score_list)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    return gen_sorted_hold_combo(hand, len(hand))
    



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = set()
    all_holds = gen_all_holds(hand)
    expected_values = []
    best_holds = []
    max_expected_value = 0.0
    for hold in all_holds:
        expected_values.append(expected_value(hold, num_die_sides, len(hand) - len(hold)))
    max_expected_value = max(expected_values)
    for hold in all_holds:
        if expected_value(hold, num_die_sides, len(hand) - len(hold)) == max_expected_value:
            best_holds.append(hold)
    
    return (max_expected_value, random.choice(best_holds))


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



