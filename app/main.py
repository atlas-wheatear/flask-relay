from flask import Flask, request, send_file
from tempfile import NamedTemporaryFile
TEMP_DIR = "/tmp"
SUFFIX = ".ogg"

app = Flask(__name__)
# ban too large uploads
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

@app.route('/', methods=['POST'])
def hello():
    ogg_file = request.files["ogg"]
    with NamedTemporaryFile(suffix=SUFFIX, dir=TEMP_DIR) as temp:
        tempfile = temp.name
        ogg_file.save(tempfile)
        return send_file(tempfile)
