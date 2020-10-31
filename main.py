WORD_INPUT = "J1ENEN092"
AFD = "automatos/afd_jenaro.txt"

def generate_states(transition):
    """Generate transition states."""
    # origin, consumed, destiny
    return [field.strip() for field in transition.split(" ")]

def read_data(name):
    """Read AFD data from file."""
    with open(name, "r") as lines:
        data = [line.strip() for line in lines]
    return data

def process_state(term, valid_transitions):
    """Process a state and return next state."""
    try:
        return valid_transitions[term]
    except KeyError as error:
        raise KeyError(f"Indefinition , Invalid Transition: {error}.")


# Load AFD data from file
data = read_data(AFD)
initial_state = data.pop(0).split(":")[1]
final_state = data.pop(0).split(":")[1]

# Generate transition states
states = {}
for t in data:
    src, consumed, destiny = generate_states(t)
    if src not in states:
        accepted = {}
        accepted[consumed] = destiny
        states[src] = accepted
    else:
        temp = states[src]
        temp[consumed] = destiny
        states[src] = temp

print(f"States: {states}")


# Process word of input
word_vector = list(WORD_INPUT)

# Begin process of word from initial states
actual_state = states[initial_state]
actual_state = process_state(word_vector.pop(0), actual_state)

for element in word_vector:
    # print(f"Word Consumed: {element}")
    # print(states[actual_state])
    try:
        actual_state = process_state(element, states[actual_state])
    except KeyError as err:
        print(f"Word Not accepted: {err}")
        exit(-1)

if actual_state == final_state:
    print("Word Accepted")
else:
    print("Word Not accepted, Fim da leitura Estado Não Final")
