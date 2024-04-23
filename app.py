from flask import Flask, jsonify, request
import os, random, azure_blob

app = Flask(__name__)
app.debug = True

def transform_word(word):
    reverse = word[::-1]
    return jsonify({'transformed': reverse.swapcase()})

def generate_random_numbers(file_path, num_numbers):
    with open(file_path, "w") as file:
        for _ in range(num_numbers):
            file.write(str(random.randint(1, 1000)) + "\n")

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

@app.route('/api/upload-random', methods=["POST"])
def upload_random():
    blob_name = "random_numbers.txt"
    container_name = "my-container"
    file_path = "random_numbers.txt"
    generate_random_numbers(file_path, 100)
    azure_blob.upload_blob(container_name, blob_name, file_path)

    return jsonify({'upload:': 'success'}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
