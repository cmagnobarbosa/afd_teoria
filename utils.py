"""
Utils file..
"""

def load_data(word_path):
    """Read data from file."""
    with open(word_path, "r") as lines:
        return [line.strip() for line in lines]
        
def format_output(transitions):
    """Return list with transitions formated."""
    return [states['transition'] for states in transitions]
