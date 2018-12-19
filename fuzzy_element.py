from flask import Flask
from fuzzywuzzy import fuzz, process

app = Flask(__name__)

# @app.route('/fuzzy/ratio/<sentences>', methods=['GET'])
@app.route('/fuzzy/ratio', methods=['GET'])
def fuzz_ratio():
    result = {}
    sample1 = fuzz.ratio('geeksforgeeks', 'geeksgeeks')
    sample2 = fuzz.ratio('GeeksforGeeks', 'GeeksforGeeks')
    sample3 = fuzz.ratio('geeks for geeks', 'Geeks For Geeks ')
    
    result["score 1"] = sample1
    result["score 2"] = sample2
    result["score 3"] = sample3

    return str(result)

    # ** Notes **
    # Ratio method matching all sentences one by one (including punctuation, spaces, and others)
    # 
    # ** Result **
    # 'geeksforgeeks', 'geeksgeeks'         : score 87
    # 'GeeksforGeeks', 'GeeksforGeeks'      : score 100
    # 'geeks for geeks', 'Geeks For Geeks ' : score 80

@app.route('/fuzzy/partial_ratio', methods=['GET'])
def partial_ratio():
    result = {}
    sample1 = fuzz.partial_ratio("geeks for geeks", "geeks for geeks!")
    sample2 = fuzz.partial_ratio("geeks for geeks", "geeks geeks")
    
    result["score 1"] = sample1
    result["score 2"] = sample2

    return str(result)

    # ** Notes **
    # Partial Ratio method is partially match words
    # In example 1 -> score 100, because partially words are same even though there is exclamation mark in second string
    # In example 2 -> score 64 (is less), because there is a extra (the extra is : for)
    #                 token in the middle middle of the string. 
    #
    # ** Result **
    # "geeks for geeks", "geeks for geeks!" : score 100
    # "geeks for geeks", "geeks geeks"      : score 64

@app.route('/fuzzy/token_ratio', methods=['GET'])
def token_ratio():
    result = {}
    sample1 = fuzz.token_sort_ratio("geeks for geeks", "for geeks geeks")
    sample2 = fuzz.token_sort_ratio("geeks for geeks", "geeks for for geeks")
    sample3 = fuzz.token_set_ratio("geeks for geeks", "geeks for for geeks")

    result["score 1"] = sample1
    result["score 2"] = sample2
    result["score 3"] = sample3

    # ** Notes **
    # Token Ratio is method string matching by token (every word)
    # In example 1 -> score 100, This gives 100 as every word is same, irrespective of the position
    # In example 2 -> score 88, Because there is two for in second sentences
    # In example 3 -> score 100, Using token_set_ratio possibility considers duplicate words as a single word. 
    #
    # ** Result **
    # "geeks for geeks", "for geeks geeks"     : score 100
    # "geeks for geeks", "geeks for for geeks" : score 88
    # "geeks for geeks", "geeks for for geeks" : score 100

    return str(result)

@app.route('/fuzzy/process', methods=['GET'])
def fuzz_process():
    query = 'geeks for geeks'
    list_text = ['geek for geek', 'geek geek', 'g. for geeks'] 
    result = {}
    sample1 = process.extract(query, list_text, limit=5)
    sample2 = process.extractOne(query, list_text)

    result["score 1"] = sample1
    result["score 2"] = sample2

    # ** Notes **
    # Process is method string matching using list
    # In example 1 -> extract, Get a list of matches ordered by score, default limit to 5 
    # In example 2 -> extractOne, we want only the top one
    #
    # ** Result **
    # Sample 1 : [('geeks geeks', 95), ('g. for geeks', 95), ('geek for geek', 93)] 
    # Sample 2 : ('geeks geeks', 95)

    return str(result)

@app.route('/fuzzy/wratio', methods=['GET'])
def fuzz_wratio():
    result = {}
    sample1 = fuzz.WRatio('geeks for geeks', 'Geeks For Geeks')
    sample2 = fuzz.WRatio('geeks for geeks!!!','geeks for geeks')
    sample3 = fuzz.ratio('geeks for geeks!!!','geeks for geeks') 

    result["score 1"] = sample1
    result["score 2"] = sample2
    result["score 3"] = sample3

    # ** Notes **
    # WRatio is method string matching which possible to handle lower and upper case and some other parameters too.
    # In example 1 -> Score 100 because using WRatio can ignore upper/lowercase and some other parameters.
    # In example 2 -> Score 100 because using WRatio can ignore upper/lowercase and some other parameters.
    # In example 3 -> Score 91 because using simple ratio will check one by one upper/lowercase and some other parameters.
    #
    # ** Result **
    # Sample 1 : score 100
    # Sample 2 : score 100
    # Sample 3 : score 91

    return str(result)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4001)