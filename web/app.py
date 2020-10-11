from flask import Flask, jsonify, make_response
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://db:27017/restdb'

mongo = PyMongo(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Invalid API call'}), 404)


def is_valid_word(str):
    # To check whether a word contains any space (i.e sentence not a word)
    if ' ' in str:
        return False

    for i in range(len(str)):
        if (((ord('a') <= ord(str[i]) <= ord('z')) or
             (ord('A') <= ord(str[i]) <= ord('Z'))) or str[i].isdigit()):
            return True
    return False


@app.route('/word/<name>', methods=['GET'])
def get_one_word(name):
    worddb = mongo.db.worldlist
    words = worddb.find_one({'word': name})
    if words:
        output = words['count']
    else:
        output = 0
    return jsonify(output)


@app.route('/word/<name>', methods=['PUT'])
def add_word(name):
    worddb = mongo.db.worldlist
    if is_valid_word(name):
        if worddb.count_documents({"word": name}) == 0:
            worddb.insert_one({'word': name, 'count': 1})
        else:
            count_temp = worddb.find({'word': name})[0]["count"]
            worddb.update_one({'word': name}, {
                "$set": {'count': count_temp + 1
                         }
            })
    else:
        output = {"Error": "Please enter the valid word of length 1 or more"}
        return jsonify(output), 400

    return ''


@app.route('/')
def word_counter():
    return "Word Counter Application"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
