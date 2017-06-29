#!/usr/bin/env python2

def StopWords():
    """
    Input: A dataframe containing the questions and some other info. 
    Output: A list of stop words (all words that apppear more than 10000 times).
    """
    from problem1 import preprocess
    import pandas as pd
    from collections import Counter
    train = pd.read_csv("training.csv", header = None, names = ["qid", "qid2", "question1", "question2", "duplicate"])


    counts = Counter(preprocess(" ".join(train['question2'].astype(str) + train["question1"].astype(str))).split())
    return [word for c, word in zip(counts.values(), counts) if c > 10000] 
    
        
def ComputeOneScore(stopWords, quest1, quest2 ):
    """
    Input: A list of stop words and two questions (each a string).
    Output: A score for how much those questions overlap. 
    """
    from problem1 import preprocess
    
    score1, score2 = 0.0, 0.0
    q1 = preprocess(quest1).split()
    q2 = preprocess(quest2).split()

    # Remove stop words from q1 and q2:
    q1 = [word for word in q1 if word not in stopWords]
    q2 = [word for word in q2 if word not in stopWords]
    
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
    import pandas as pd
    import sys
    import numpy as np
    from problem3 import ComputeAccuracy
    
    train = pd.read_csv(sys.argv[1], header = None, names = ["qid", "qid2", "question1", "question2", "duplicate"])
    stopWords = StopWords()
    thr = float(sys.argv[2])

    # Get the testing accuracy:
    correctCount = 0.0 # Keeps track of the number of correct predictions
    # For each row:
    for index, row in train.iterrows():    
        # Get the score:
        try: score = ComputeOneScore(stopWords, row["question1"], row["question2"])
        except: score = 0.0

        correctCount = correctCount + ComputeAccuracy(row, thr, score)

    # Show the accuracy for that threshold:
    print correctCount / len(train)

if __name__ == "__main__": main()
