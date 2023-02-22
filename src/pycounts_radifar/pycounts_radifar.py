from collections import Counter
from string import punctuation
from typing import Type


def load_text(input_file: str) -> str:
    """Load text from a text file and return as a string.

    Parameters
    ----------
    input_file : str
        a text file
    """
    with open(input_file, "r") as file:
        text = file.read()
    return text


def clean_text(text: str) -> str:
    """Lowercase and remove punctuation from a string.

    Parameters
    ----------
    text : str
        the content of input_file
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file: str) -> Type[Counter]:
    """Count unique words in a string.

    Parameters
    ----------
    input_file : str
        a text file
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
