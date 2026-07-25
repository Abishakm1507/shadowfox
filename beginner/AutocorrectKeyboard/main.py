"""
Autocorrect Keyboard System with Trigram Next-Word Prediction
=============================================================

A console-based autocorrect keyboard that:
1. Detects and corrects misspelled words using pyspellchecker
2. Predicts the next word using a Trigram Language Model

"""

import re
import string
import os
from collections import defaultdict, Counter
from spellchecker import SpellChecker


def load_corpus(filepath: str = "corpus.txt") -> str:
    """
    Load the text corpus from a file.

    Args:
        filepath: Path to the corpus text file.

    Returns:
        The entire corpus as a single string.

    Raises:
        FileNotFoundError: If the corpus file does not exist.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Corpus file '{filepath}' not found.")

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def preprocess_text(text: str) -> list:
    """
    Preprocess text by converting to lowercase, removing punctuation,
    and splitting into tokens.

    Args:
        text: Raw input text string.

    Returns:
        A list of lowercase word tokens without punctuation.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation (keep apostrophes for contractions like "don't")
    text = text.translate(str.maketrans("", "", string.punctuation.replace("'", "")))
    # Split into words
    words = text.split()
    return words


def build_bigram_model(tokens: list) -> dict:
    """
    Build a bigram language model from a list of tokens.

    A bigram model counts how often a word follows another word.
    Structure: {word1: {word2: count}}

    Args:
        tokens: List of preprocessed word tokens.

    Returns:
        Dictionary mapping each word to a Counter of following words.
    """
    bigram_model = defaultdict(Counter)

    for i in range(len(tokens) - 1):
        word1 = tokens[i]
        word2 = tokens[i + 1]
        bigram_model[word1][word2] += 1

    return dict(bigram_model)


def build_trigram_model(tokens: list) -> dict:
    """
    Build a trigram language model from a list of tokens.

    A trigram model counts how often a word follows a pair of words.
    Structure: {(word1, word2): {word3: count}}

    Args:
        tokens: List of preprocessed word tokens.

    Returns:
        Dictionary mapping each word pair (tuple) to a Counter of following words.
    """
    trigram_model = defaultdict(Counter)

    for i in range(len(tokens) - 2):
        word1 = tokens[i]
        word2 = tokens[i + 1]
        word3 = tokens[i + 2]
        trigram_model[(word1, word2)][word3] += 1

    return dict(trigram_model)


def autocorrect_sentence(sentence: str, spell: SpellChecker) -> tuple:
    """
    Detect and correct misspelled words in a sentence.

    Preserves punctuation and restores original capitalization.

    Args:
        sentence: The input sentence string.
        spell: An initialized SpellChecker instance.

    Returns:
        A tuple containing:
        - corrected_sentence (str): The sentence with corrections applied.
        - corrections (list): List of (original, corrected) tuples for misspelled words.
        - stats (dict): Statistics about the correction process.
    """
    # Split into words while preserving surrounding punctuation
    raw_words = re.findall(r"\b\w+\b|[^\w\s]", sentence)

    corrected_words = []
    corrections = []
    misspelled_count = 0
    correct_count = 0

    for word in raw_words:
        # Skip punctuation and empty strings
        if not word or not word.isalpha():
            corrected_words.append(word)
            continue

        # Check if the word is misspelled (case-insensitive)
        is_misspelled = spell.unknown([word.lower()])

        if word.lower() in is_misspelled:
            # Get the most likely correction
            correction = spell.correction(word.lower())

            if correction and correction != word.lower():
                corrections.append((word, correction))
                misspelled_count += 1
                # Preserve original capitalization
                if word[0].isupper():
                    correction = correction.capitalize()
                corrected_words.append(correction)
            else:
                corrected_words.append(word)
                correct_count += 1
        else:
            corrected_words.append(word)
            correct_count += 1

    # Reconstruct sentence with proper spacing
    corrected_sentence = ""

    for i, token in enumerate(corrected_words):
        if token in string.punctuation:
            # Attach punctuation directly to previous word (no space before)
            corrected_sentence = corrected_sentence.rstrip() + token + " "
        else:
            if i == 0:
                corrected_sentence += token
            else:
                corrected_sentence += " " + token

    corrected_sentence = corrected_sentence.strip()

    # Restore first-letter capitalization
    if corrected_sentence and corrected_sentence[0].islower():
        corrected_sentence = corrected_sentence[0].upper() + corrected_sentence[1:]

    stats = {
        "total_words": len(corrections) + correct_count,
        "correct_words": correct_count,
        "misspelled_words": misspelled_count,
        "corrections_made": len(corrections),
    }

    return corrected_sentence, corrections, stats


def predict_next_word(
    context: str,
    trigram_model: dict,
    bigram_model: dict,
) -> str:
    """
    Predict the next word using trigram model with bigram fallback.

    First tries to find the most frequent word following the last two words
    (trigram). If not found, falls back to the last word only (bigram).

    Args:
        context: The input context string (e.g., "I love").
        trigram_model: The trigram frequency dictionary.
        bigram_model: The bigram frequency dictionary.

    Returns:
        The predicted next word, or a message if no prediction is available.
    """
    # Preprocess the context
    context_tokens = preprocess_text(context)

    if len(context_tokens) < 1:
        return "No prediction available."

    # Try trigram prediction first (needs at least 2 words)
    if len(context_tokens) >= 2:
        last_two = (context_tokens[-2], context_tokens[-1])
        if last_two in trigram_model:
            # Get the most frequent next word
            predicted_word = trigram_model[last_two].most_common(1)[0][0]
            return predicted_word

    # Fallback to bigram prediction (needs at least 1 word)
    if len(context_tokens) >= 1:
        last_word = context_tokens[-1]
        if last_word in bigram_model:
            predicted_word = bigram_model[last_word].most_common(1)[0][0]
            return predicted_word

    return "No prediction available."


def display_corrections(corrections: list) -> None:
    """
    Display the list of word corrections in a formatted way.

    Args:
        corrections: List of (original, corrected) tuples.
    """
    if not corrections:
        print("\nNo corrections needed. All words are spelled correctly!")
        return

    print("\n" + "=" * 50)
    print("CORRECTIONS")
    print("=" * 50)
    for original, corrected in corrections:
        print(f"  {original} -> {corrected}")


def display_statistics(stats: dict, prediction_type: str) -> None:
    """
    Display typing statistics after processing a sentence.

    Args:
        stats: Dictionary containing word counts and correction stats.
        prediction_type: String indicating which model was used for prediction.
    """
    print("\n" + "=" * 50)
    print("TYPING STATISTICS")
    print("=" * 50)
    print(f"  Total Words:      {stats['total_words']}")
    print(f"  Correct Words:    {stats['correct_words']}")
    print(f"  Misspelled Words: {stats['misspelled_words']}")
    print(f"  Corrections Made: {stats['corrections_made']}")
    print(f"  Prediction Used:  {prediction_type}")


def main() -> None:
    """
    Main program entry point.

    Loads the corpus, builds language models, and runs the
    interactive autocorrect keyboard loop.
    """
    print("=" * 60)
    print("         AUTOCORRECT KEYBOARD SYSTEM")
    print("   with Trigram Next-Word Prediction")
    print("=" * 60)

    # Initialize the spell checker
    spell = SpellChecker()

    # Load and preprocess the corpus
    try:
        print("\nLoading corpus and building language models...")
        corpus_text = load_corpus()
        corpus_tokens = preprocess_text(corpus_text)

        # Build language models
        bigram_model = build_bigram_model(corpus_tokens)
        trigram_model = build_trigram_model(corpus_tokens)

        print(f"Corpus loaded: {len(corpus_tokens)} words, "
              f"{len(bigram_model)} bigrams, "
              f"{len(trigram_model)} trigrams")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure 'corpus.txt' exists in the project directory.")
        return

    # Main interaction loop
    while True:
        print("\n" + "-" * 60)
        print("Enter a sentence (or type 'exit' to quit, 'help' for commands):")
        print("-" * 60)

        user_input = input("\n> ").strip()

        # Handle special commands
        if user_input.lower() == "exit":
            print("\nThank you for using the Autocorrect Keyboard System!")
            print("Goodbye!")
            break

        if user_input.lower() == "help":
            print("\nAvailable commands:")
            print("  <sentence>  - Type any sentence to autocorrect and predict")
            print("  exit        - Exit the program")
            print("  help        - Show this help message")
            continue

        if not user_input:
            print("Please enter a valid sentence.")
            continue

        # Part 1: Autocorrect the sentence
        corrected_sentence, corrections, stats = autocorrect_sentence(
            user_input, spell
        )

        # Display original and corrected sentences
        print("\n" + "=" * 50)
        print("ORIGINAL SENTENCE")
        print("=" * 50)
        print(f"  {user_input}")

        print("\n" + "=" * 50)
        print("CORRECTED SENTENCE")
        print("=" * 50)
        print(f"  {corrected_sentence}")

        # Display corrections
        display_corrections(corrections)

        # Part 2: Predict next word
        print("\n" + "=" * 50)
        print("NEXT WORD PREDICTION")
        print("=" * 50)

        # Use the corrected sentence for prediction context
        prediction_context = preprocess_text(corrected_sentence)

        # Determine prediction type
        prediction_type = "Trigram"
        if len(prediction_context) >= 2:
            last_two = (prediction_context[-2], prediction_context[-1])
            if last_two not in trigram_model:
                prediction_type = "Bigram (Trigram not found, fallback)"
        elif len(prediction_context) == 1:
            prediction_type = "Bigram (only one word in context)"

        # Get the prediction
        prediction = predict_next_word(
            corrected_sentence, trigram_model, bigram_model
        )

        # Show the context used for prediction
        context_words = prediction_context[-2:] if len(prediction_context) >= 2 else prediction_context
        context_display = " ".join(context_words) if context_words else "(empty)"
        print(f"\n  Input Context: {context_display}")
        print(f"  Prediction:    {prediction}")

        # Display statistics
        display_statistics(stats, prediction_type)

        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
