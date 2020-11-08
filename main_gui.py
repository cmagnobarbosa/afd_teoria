"""Módulo WEB GUI."""
import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from afd import generate_DFA, check_word
from utils import format_output, load_data

import webbrowser

app = Flask(__name__)

# Path to save files with multiples words
UPLOAD_FOLDER = 'upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Gera automato finito Deterministico
# Generate DFA
states, initial_state, final_state = generate_DFA()

@app.route('/')
def index():
    """
    Return index.html
    Retorna a pagina inicial.
    """
    return render_template('index.html')


@app.route('/check_word', methods=['POST'])
def check_word_gui():
    """
    Check if word is accept by DFA.
    Recebe uma palavra e verifica se a mesma é aceita pelo automato.
    """
    # Get word send by form
    word = request.form.get('word')

    if not word:
        return render_template('index.html')
    # Check if a word is accepted in AFD.
    response, transitions = check_word(word, states,
                                         initial_state, final_state)
    return render_template('index.html', status=response, log=transitions)


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Receive a file from form and check the words in file.
    Recebe as palavras enviadas através do formulário e verifica cada palavra
    no arquivo.
    """
    # Get file submitted by form
    file = request.files.get('file')

    # if a file is not sended return home
    if not file:
        return render_template('index.html')

    # save uploaded file, wih multiple words to check
    filename = secure_filename(file.filename)
    path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path_to_save)

    # return a list with words in file; A word by line.
    # carrega as palavras, uma palavra por linha(Eg. palavras_aceitas)
    words = load_data(path_to_save)

    responses = []
    # verifica as palavras presentes no arquivo
    # verifica cada palavra
    for word in words:
        # Check if a word is accepted in AFD.
        # verifica se a palavra é aceita pelo automato
        response, transitions = check_word(word, states,
                                             initial_state, final_state)
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
