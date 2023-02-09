from flask import Flask
import logging
import json

app = Flask(__name__)

@app.route('/palindrome/<word>')
def palindrome(word):
    logging.info("Word received: [" + str(word) + "]")
    jsonResponse = buildJSON(word)
    logging.info("JSON obtained: {" + jsonResponse + "}")
    return jsonResponse

def buildJSON(word):
    flag = False
    args = word 
    #Remove the spaces from string
    palindrome = args.replace(" ","").lower()
    listToString = "".join(palindrome)
    stringReversed = listToString[::-1]
    listToStringReversed = "".join(stringReversed)

    if listToString == listToStringReversed:
        flag = True
        #Iterate through the string and sort it. 
        x = [i for i in listToStringReversed]
        x.sort()
        z = x

        freq = {}
        for i in z:
            freq[i] = z.count(i)

        length = len(x)
        
        dictionary = {
            'name': listToString,
            'palindrome': flag,
            'sorted': freq,
            'length': length
        }

        jsonToString = json.dumps(dictionary)
        return jsonToString

    else:
        dictionary = {
            'name': listToString,
            'palindrome': flag,
        }
        jsonToString = json.dumps(dictionary)
        return jsonToString


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, debug=False)