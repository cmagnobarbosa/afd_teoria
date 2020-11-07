"""
Utils file..
"""

def format_output(transitions):
    """Return list with transitions formated."""
    return [states['transition'] for states in transitions]
