"""Módulo WEB GUI."""
import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from main import load_data, process_word
from utils import format_output

import webbrowser

app = Flask(__name__)

# Path to save files with multiples words
UPLOAD_FOLDER = 'upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    """Return index.html ."""
    return render_template('index.html')


@app.route('/check_word', methods=['POST'])
def check_word():
    """Check if word is accepted in AFD."""
    # Get word send by form
    word = request.form.get('word', 'Noboby here')

    # Check if a word is accepted in AFD.
    response, transitions = process_word(word)
    return render_template('index.html', status=response, log=transitions)


@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload a file and check multiple words."""
    # Get file send by form
    file = request.files.get('file')

    # if a file is not sended return home
    if not file:
        return render_template('index.html')

    # save uploaded file, wih multiple words to check
    filename = secure_filename(file.filename)
    path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path_to_save)

    # return a list with words in file; A word by line.
    words = load_data(path_to_save)

    responses = []
    for word in words:
        # Check if a word is accepted in AFD.
        response, transitions = process_word(word)
        responses.append({"word": word, "status": response,
                          "transition": format_output(transitions)})
    return render_template('multiples_words.html', multiples_words=responses)


# main method
if __name__ == "__main__":
    print("Carregando interface, O navegador irá abrir automaticamente.")
    print("Caso não abra acesse http://localhost:5000/")
    webbrowser.open_new('http://localhost:5000/')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
