"""Módulo Principal TP teoria de Linguagens."""
from graphviz import Digraph

# Load AFD from file
AFD = "automatos/afd.txt"
dot = Digraph(comment='AFD Loaded')


def generate_states(transition):
    """Generate transition states."""
    # origin, consumed, destiny
    return [field.strip() for field in transition.split(" ")]


def load_data(word_path):
    """Read data from file."""
    with open(word_path, "r") as lines:
        return [line.strip() for line in lines]


def process_state(term, valid_transitions):
    """Process a state and return next state."""
    try:
        return valid_transitions[term]
    except KeyError as error:
        raise KeyError(f"Indefinition , Invalid Transition: {error}.")


# Load AFD data from file
data = load_data(AFD)
initial_state = data.pop(0).split(":")[1]
final_state = data.pop(0).split(":")[1]

# Generate transition states
states = {}
print(f'Initial state: {initial_state}')
print(f"Final state: {final_state}")

dot.node(initial_state, color="black", style='bold')
dot.node(final_state, color="green", shape='doublecircle', style="bold")
for t in data:
    src, consumed, destiny = generate_states(t)
    dot.node(src)
    dot.node(destiny)
    dot.edge(src, destiny, consumed)
    if src not in states:
        accepted = {}
        accepted[consumed] = destiny
        states[src] = accepted
    else:
        temp = states[src]
        temp[consumed] = destiny
        states[src] = temp

print(f"States: {states}")
dot.render('static/imgs/afd_plot', view=True)


def process_word(word, detail_steps=True):
    """Process a word."""
    transitions_log = []
    response_state = ''
    # words = load_data(words_file)
    print(f"Word Loaded: {word}")
    # Process word of input
    word_vector = list(word)

    # Begin process of word from initial states
    actual_state = states[initial_state]
    try:
        actual_state = process_state(word_vector.pop(0), actual_state)
    except KeyError:
        return 'Word Not accepted, Indefinition', []
    if detail_steps:
        t_log = {"word": word[0],
                 "transition": f"{initial_state} -> {actual_state}"}
        print(t_log)
        transitions_log.append(t_log)

    # Check any element the word.
    # Verifica cada caracter da palavra
    for element in word_vector:
        try:
            old_state = actual_state
            actual_state = process_state(element, states[actual_state])

            # Exibe cada transição realizada
            if detail_steps:
                t_log = {"word": element,
                         "transition": f"{old_state}->{actual_state}"}
                print(t_log)
                transitions_log.append(t_log)
        except KeyError as err:
            print(f"Word Not accepted: {err}")
            response_state = "Word Not accepted, Indefinition"
            return response_state, transitions_log

    if actual_state == final_state:
        print("Word Accepted")
        response_state = 'Word Accepted'
        print("\n------------------------\n")
    else:
        print("Word Not accepted, Fim da leitura Estado Não Final")
        response_state = 'Word Not Accepted, Estado Não Final'
    return response_state, transitions_log
