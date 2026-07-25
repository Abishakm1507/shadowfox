# Autocorrect Keyboard System with Trigram Next-Word Prediction

A console-based autocorrect keyboard system that detects misspelled words, automatically corrects them, and predicts the next word using a Trigram Language Model. Built for the ShadowFox Internship task submission.

## Objective

Develop a console-based autocorrect keyboard that:
- Detects misspelled words using the `pyspellchecker` library
- Automatically corrects them
- Predicts the next word using a Trigram Language Model built from scratch

The project demonstrates basic Natural Language Processing (NLP) concepts while remaining simple, beginner-friendly, and easy to understand.

## Features

- **Spell Check & Autocorrect**: Detects and corrects misspelled words using `pyspellchecker`
- **Punctuation Preservation**: Maintains punctuation in the corrected output
- **Capitalization Restoration**: Restores proper sentence capitalization
- **Trigram Next-Word Prediction**: Predicts the next word using a trigram language model
- **Bigram Fallback**: Falls back to bigram prediction if trigram context is unavailable
- **Typing Statistics**: Displays total words, correct words, misspelled words, and corrections made
- **Interactive Console Interface**: Simple command-line interface with help commands

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| pyspellchecker | Spell checking and correction library |
| collections (defaultdict, Counter) | Building trigram and bigram frequency models |
| re | Regular expressions for text processing |
| string | Punctuation handling |
| os | File path operations |

## Folder Structure

```
AutocorrectKeyboard/
│
├── main.py              # Main application code
├── corpus.txt           # Training corpus for language models
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation (this file)
│
└── screenshots/        # Screenshots directory
    ├── autocorrect.png  # Screenshot of autocorrect feature
    └── prediction.png   # Screenshot of prediction feature
```

## Installation

### Prerequisites
- Python 3.6 or higher installed on your system
- pip (Python package installer)

### Steps

1. **Clone or download the project**
   ```
   cd AutocorrectKeyboard
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

## How to Run

```bash
cd AutocorrectKeyboard
python main.py
```

### Usage

1. Run the program using the command above
2. The program will load the corpus and build language models
3. Type any sentence and press Enter to:
   - See the corrected version
   - View a list of corrections made
   - Get a prediction for the next word
   - View typing statistics
4. Type `exit` to quit the program
5. Type `help` to see available commands

### Example Interaction

```
============================================================
         AUTOCORRECT KEYBOARD SYSTEM
   with Trigram Next-Word Prediction
============================================================

Loading corpus and building language models...
Corpus loaded: 520 words, 304 bigrams, 298 trigrams

------------------------------------------------------------
Enter a sentence (or type 'exit' to quit, 'help' for commands):
------------------------------------------------------------

> I hav a dreem

==================================================
ORIGINAL SENTENCE
==================================================
  I hav a dreem

==================================================
CORRECTED SENTENCE
==================================================
  I have a dream

==================================================
CORRECTIONS
==================================================
  hav -> have
  dreem -> dream

==================================================
NEXT WORD PREDICTION
==================================================

  Input Context: a dream
  Prediction:    to

==================================================
TYPING STATISTICS
==================================================
  Total Words:      4
  Correct Words:    2
  Misspelled Words: 2
  Corrections Made: 2
  Prediction Used:  Trigram

============================================================
```

## Trigram Algorithm Explanation

### What is a Trigram?

A trigram is a sequence of three consecutive words. In language modeling, a trigram model predicts the probability of a word given the two preceding words.

**Formula:**
```
P(word3 | word1, word2) = count(word1, word2, word3) / count(word1, word2)
```

### How It Works

1. **Training**: The program reads the corpus and counts how often each three-word sequence appears.

   **Example corpus:**
   ```
   I love machine learning.
   I love artificial intelligence.
   I love programming.
   ```

   **Generated trigrams:**
   ```
   (I, love) → machine (1 occurrence)
   (love, machine) → learning (1 occurrence)
   (I, love) → artificial (1 occurrence)
   (love, artificial) → intelligence (1 occurrence)
   (I, love) → programming (1 occurrence)
   (love, programming) → (no following word)
   ```

2. **Storage**: Frequencies are stored using dictionaries:
   ```python
   trigram_model = {
       ("I", "love"): {"machine": 1, "artificial": 1, "programming": 1},
       ("love", "machine"): {"learning": 1},
       ("love", "artificial"): {"intelligence": 1}
   }
   ```

3. **Prediction**: When the user types "I love", the program:
   - Looks up the context pair ("I", "love") in the trigram model
   - Finds three possible next words: "machine", "artificial", "programming"
   - Selects the most frequent one (all equally frequent here, picks the first)

4. **Fallback**: If the context pair isn't found in the trigram model:
   - Falls back to the bigram model
   - Uses only the last word to make a prediction
   - Example: If ("new", "world") doesn't exist, searches using just "world"

### Bigram Model (Fallback)

A bigram is a sequence of two words. It predicts the next word based on only the last word:

```python
bigram_model = {
    "love": {"machine": 1, "artificial": 1, "programming": 1},
    "machine": {"learning": 1}
}
```

## Autocorrect Workflow

1. **Input**: User types a sentence (e.g., "I hav a dreem")
2. **Tokenization**: Sentence is split into individual words
3. **Spell Checking**: Each word is checked against the `pyspellchecker` dictionary
4. **Correction**: Misspelled words are replaced with the most probable correct spelling
5. **Preservation**: Original punctuation and capitalization are restored in the output
6. **Display**: Original sentence, corrected sentence, and a list of corrections are shown
7. **Prediction**: The corrected sentence is used as context for next-word prediction
8. **Statistics**: Word counts and prediction type are displayed

## Future Improvements

- **Add a larger corpus**: Improve prediction accuracy with more training data
- **Implement caching**: Speed up repeated predictions
- **Add word suggestions**: Show multiple word suggestions instead of just the top one
- **Support for autocorrect history**: Track frequently used corrections
- **Add a GUI**: Build a simple graphical interface
- **Implement n-gram smoothing**: Better handle unseen trigrams
- **Add custom dictionary**: Allow users to add custom words
- **Support multiple languages**: Extend spell checking to other languages

## License

This project is created for the ShadowFox Internship program.

## Author

ShadowFox Intern