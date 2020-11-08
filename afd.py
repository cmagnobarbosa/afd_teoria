"""Módulo Principal TP teoria de Linguagens."""
from graphviz import Digraph
from utils import load_data

# Load DFA from file
AFD = "automatos/afd.txt"

# Utilizado para plot do AFD gerado.
# Used to plot DFA
# Used only to plot
# O graphiz somente é Utilizado para o plot
dot = Digraph(comment='AFD Loaded')


def generate_states(transition):
    """Generate transition states."""
    # origin, consumed, destiny
    return [field.strip() for field in transition.split(" ")]

def process_state(term, valid_transitions):
    """Process a state and return next state."""
    try:
        return valid_transitions[term]
    except KeyError as error:
        raise KeyError(f"Indefinition , Invalid Transition: {error}.")

def generate_DFA():
    """
    Generate DFA(Deterministic finite automaton).
    Gera o AFD(Autômato finito Deterministico).
    """
    # Load data to generate DFA
    data = load_data(AFD)
    initial_state = data.pop(0).split(":")[1]
    final_state = data.pop(0).split(":")[1]

    # Generate transition states
    states = {}
    print(f'Initial state: {initial_state}')
    print(f"Final state: {final_state}")

    # Add initial and final state to plot
    dot.node(initial_state, color="black", style='bold')
    dot.node(final_state, color="green", shape='doublecircle', style="bold")

    # DFA, AFD
    # Generate a dictionary with valid transitions
    # {'estado': {'termo_aceito': 'proximo_estado'}}
    for t in data:
        # src: source state
        # consumed: accepted word
        # destiny: next state
        src, consumed, destiny = generate_states(t)

        # used in plot
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

    print('AFD carregado')
    print(f"DFA States: {states}")

    # Exibe o autômato gerado
    # plot DFA
    dot.render('static/imgs/afd_plot', view=True)
    return states, initial_state, final_state


def check_word(word, states, initial_state, final_state):
    """Check if a word is accepted by DFA."""
    detail_steps=True
    transitions_log = []
    response_state = ''

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
            # verifica se a letra possui uma transição valida,
            # se sim retorna o próximo estado
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
        response_state = 'Word Not Accepted, Final state not reached'
    return response_state, transitions_log
