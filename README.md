# fuzzy-python-flask
Fuzzy String Matching (Using Python Flask)

Using:
1. python3
2. flask
3. fuzzywuzzy

Installation :
1. Create virtualenv if you want to use it and activate :
    - virtualenv venv
    - source venv/bin/activate
    
2. Install requirements.txt :
    - pip install -r requirements
    - We need package :
        - flask
        - fuzzywuzzy

3. Run the script :
    - python fuzzy_element.py
    * note : 
        - this script contains the method in the fuzzywuzzy package
        - there are several endpoints for each method
    * for trying that script you can test one of endpoint in your browser , example :
        1. http://127.0.0.1:4001/fuzzy/wratio (url for wratio method)
        2. http://127.0.0.1:4001/fuzzy/partial_ratio (url for partial ratio method)

    - python fuzzy_simple_faq.py
    * note : 
        - this script contains a simple flow faq for order food that called "rengginang"