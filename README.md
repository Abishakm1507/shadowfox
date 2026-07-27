# ShadowFox Internship Projects

A collection of three independent projects completed as part of the **ShadowFox Internship** program. Each project lives in its own folder and demonstrates different skills in Python, NLP, data analysis, and modern AI tooling.

| Project | Folder | Focus |
|---------|--------|-------|
| Autocorrect Keyboard System | `AutocorrectKeyboard/` | NLP · Spell correction · Trigram language model |
| Store Sales & Profit Analysis | `Store-Sales-and-Profit-Analysis/` | EDA · Data visualization · Business insights |
| AI-Driven NLP with LangChain & Gemini | `AI_Driven_NLP_Project/` | LLMs · Prompt engineering · LangChain |

---

## 1. Autocorrect Keyboard System with Trigram Next-Word Prediction

**Folder:** [`AutocorrectKeyboard/`](./AutocorrectKeyboard/)

A console-based autocorrect keyboard that detects misspelled words, automatically corrects them, and predicts the next word using a **Trigram Language Model** built from scratch.

### Highlights
- Spell checking & autocorrect with `pyspellchecker`
- Punctuation and capitalization preservation
- Trigram next-word prediction with bigram fallback
- Interactive CLI with typing statistics

### Tech Stack
Python 3 · pyspellchecker · collections · re

### Quick Start
```bash
cd AutocorrectKeyboard
pip install -r requirements.txt
python main.py
```

See the full documentation inside the project folder:  
[`AutocorrectKeyboard/README.md`](./AutocorrectKeyboard/README.md)

---

## 2. Store Sales and Profit Analysis

**Folder:** [`Store-Sales-and-Profit-Analysis/`](./Store-Sales-and-Profit-Analysis/)

Comprehensive Exploratory Data Analysis (EDA) on retail store sales and profit data. Uncovers trends across product categories, regions, customer segments, shipping modes, and time periods.

### Highlights
- Data cleaning & preprocessing
- Category / region / segment-wise sales & profit analysis
- Monthly & yearly trend analysis
- Correlation analysis and business insights
- Visualizations with Matplotlib & Seaborn

### Tech Stack
Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook

### Quick Start
```bash
cd Store-Sales-and-Profit-Analysis
pip install pandas numpy matplotlib seaborn
jupyter notebook SuperStore.ipynb
```

See the full documentation inside the project folder:  
[`Store-Sales-and-Profit-Analysis/README.md`](./Store-Sales-and-Profit-Analysis/README.md)

---

## 3. AI-Driven Natural Language Processing Project

**Folder:** [`AI_Driven_NLP_Project/`](./AI_Driven_NLP_Project/)

A complete NLP application built with **LangChain** and the **Google Gemini API**. Covers prompt engineering strategies, seven core NLP tasks, performance analysis, and ethical considerations.

### Highlights
- Integration of Google Gemini 3.5 Flash via LangChain
- Five prompt engineering techniques (Simple, Detailed, Role, Few-Shot, Chain-of-Thought)
- NLP tasks: Summarization, Sentiment Analysis, Classification, Keyword Extraction, QA, Translation, Grammar Correction
- Performance visualization and research experiments

### Tech Stack
Python 3.10+ · LangChain · Google Gemini · Pandas · Matplotlib · Seaborn · python-dotenv · Jupyter

### Quick Start
```bash
cd AI_Driven_NLP_Project
pip install -r requirements.txt
cp .env.example .env          # add your GEMINI_API_KEY
jupyter notebook AI_Driven_NLP_Project.ipynb
```

See the full documentation inside the project folder:  
[`AI_Driven_NLP_Project/README.md`](./AI_Driven_NLP_Project/README.md)

---

## Repository Structure

```
.
├── AutocorrectKeyboard/
│   ├── main.py
│   ├── corpus.txt
│   ├── requirements.txt
│   └── README.md
│
├── Store-Sales-and-Profit-Analysis/
│   ├── SuperStore.ipynb
│   ├── SampleSuperstore.csv
│   └── README.md
│
├── AI_Driven_NLP_Project/
│   ├── AI_Driven_NLP_Project.ipynb
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
└── README.md                 
```



These projects were created for the ShadowFox Internship program.
```
