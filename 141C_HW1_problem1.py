#!/usr/bin/env python2

def preprocess(str_in):
    """
    Input: A string
    Output: That string with all lowercase letters, unwanted punctuation replaced with whitespace, and all "-" removed. 
    """
    # Catch NaNs:
    try: str_out = str_in.lower() # Convert to lower case
    except: return str_in

    # Remove unwanted puncutaion:
    unwanted = ["?", "!", ".", "(", ")", "'", '"', ":", ","]
    
    for char in unwanted:
        str_out = str_out.replace(char, " ")
        
    str_out = str_out.replace("-", "")
    
    return str_out
