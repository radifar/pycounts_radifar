import matplotlib.pyplot as plt
from collections import Counter
from typing import Type


def plot_words(word_counts: Type[Counter], n: int = 10) -> Type[plt.bar]:
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig
