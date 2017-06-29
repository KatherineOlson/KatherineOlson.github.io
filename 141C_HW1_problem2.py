#!/usr/bin/env python2

import sys
import pandas as pd
from problem1 import preprocess

# Compute scores function:
def ComputeOneScore(quest1, quest2):
    from problem1 import preprocess
    
    """
    Input: Two questions - each as a string.
    Output: A score for how much those questions overlap. 
    """
    score1, score2 = 0.0, 0.0
    q1 = preprocess(quest1).split()
    q2 = preprocess(quest2).split()
    
    # Compute score:
    for word1 in q1:
        if word1 in q2:
            score1 = score1 + 1
    for word2 in q2:
        if word2 in q1:
            score2 = score2 + 1    
    score = (score1 + score2) / (len(q1) + len(q2))
    return  score

def main():
    # Read in data:
    train = pd.read_csv(sys.argv[1], header = None, names = ["qid", "qid2", "question1", "question2", "duplicate"])
    
    # Loop over each row of the data to compute score:
    for index, row in train.iterrows():
        # Catch NaNs and get score:
        try: score = ComputeOneScore(row["question1"], row["question2"])
        except: score = 0

        print score
    
if __name__ == '__main__':  main()
