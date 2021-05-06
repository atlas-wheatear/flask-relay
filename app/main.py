from flask import Flask, request, jsonify
from uuid import uuid4

UPLOAD_DIR = "/uploads/"
SUFFIX = ".ogg"

app = Flask(__name__)

# ban too large uploads
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

@app.route('/', methods=['POST'])
def upload_ogg():
    ogg_file = request.files["ogg"]
    hex = uuid4().hex
    filename = UPLOAD_DIR + hex + SUFFIX
    ogg_file.save(filename)
    return jsonify({
        "uuid": hex
    })


