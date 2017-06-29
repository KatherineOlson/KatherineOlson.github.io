#!/usr/bin/env python2

def ComputeAccuracy(row, thr, score):
    """
    Input: A row of data, the threshold, and the score. 
    Output: 1 if the prediction for that row was correct and 0 otherwise. 
    """
    import numpy as np
    
    # Find the label:
    label = np.sign(score - thr)
    
    # If correctly predicted a duplicate, increase correctCount:
    if label >=  0 and row["duplicate"] == 1: 
        correct = 1
    # If correctly predicted a non-duplicate, increase correctCount:
    elif label < 0 and row["duplicate"] == 0: 
        correct = 1
    # Prediction was wrong:
    else:
        correct = 0

    return correct 

def main():

    import sys
    import pandas as pd
    from problem2 import ComputeOneScore

    # Read in data and command line arguments:
    train = pd.read_csv(sys.argv[1], header = None, names = ["qid", "qid2", "question1", "question2", "duplicate"])
    thr = float(sys.argv[2])

    # Get the testing accuracy:
    correctCount = 0.0 # Keeps track of the number of correct predictions
    # For each row:
    for index, row in train.iterrows():
        # Get the score:
        try: score = ComputeOneScore(row["question1"], row["question2"])
        except: score = 0.0
        
        correctCount = correctCount + ComputeAccuracy(row, thr, score)

    # Show the accuracy for that threshold:
    print correctCount / len(train)

if __name__ == "__main__": main()
