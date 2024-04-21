from flask import Flask, jsonify, request
import os

app = Flask(__name__)
app.debug = True

def transform_word(word):
    reverse = word[::-1]
    return jsonify({'transformed': reverse.swapcase()})

@app.route('/api/mirror')
def mirror_word():
    word = request.args.get('word')
    if word:
        return transform_word(word)
    else:
        return 'Please provide a word to mirror.'

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
