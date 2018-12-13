from flask import Flask
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

app = Flask(__name__)

@app.route('/fuzzy/api/v1.0/tasks/<string:sentences>', methods=['GET'])
def get_answer(sentences):
    return sentences
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4001)