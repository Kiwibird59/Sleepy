#Helper Functions and GLOBAL CONSTANTS

""" Converts AFINN-111.txt to a dict and returns it
"""
def create_afinn_dict():
    scores = {}
    afinn = open("AFINN-111.txt")
    for line in afinn:
        word, score = line.split("\t")
        scores[word] = int(score)
    return scores
"""GLOBAL CONSTANTS
"""
MOON_PHASE = [ 'New', 'First' ,'Full' ,'Last']
MOON_DICT_13 = {'Oct': {5: 0, 11: 1 ,18: 2 , 26: 3}, 'Nov': {3: 0, 10: 1, 17: 2, 25: 3}, 'Dec' : {3: 0, 9: 1, 17: 2, 25: 3}}
