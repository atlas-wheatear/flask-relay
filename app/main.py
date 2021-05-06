from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from uuid import uuid4

UPLOAD_DIR = "/uploads/"
EXTENSION = "ogg"
SUFFIX = f".{EXTENSION}"

app = Flask(__name__)

# ban too large uploads
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


def get_filename(uuid: str):
    secure = secure_filename(uuid)
    return f"{UPLOAD_DIR}{secure}{SUFFIX}"

@app.route('/', methods=['POST'])
def upload_ogg():
    ogg_file = request.files[EXTENSION]
    uuid = uuid4().hex
    filename = get_filename(uuid)
    ogg_file.save(filename)
    return jsonify({
        "uuid": uuid
    })

@app.route("/dl", methods=['GET'])
def get_ogg():
    uuid = request.json["uuid"]
    filename = get_filename(uuid)
    return send_file(filename)
