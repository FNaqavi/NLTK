# nltk
natural language processing example codes.

# Text Summarization using NLTK

This Python script demonstrates text summarization using the Natural Language Toolkit (NLTK). It generates a summary of input text by selecting the top-ranked sentences based on word frequency.

## Requirements

- Python 3.x
- NLTK library

Install NLTK using pip if you haven't already:

pip install nltk

## Usage

1. Run the script in a Python environment.
2. You will be prompted to enter your text. Input the text you want to summarize.
3. The script will generate a summary of the input text using NLTK.

## How it works

1. **Input Text**: The script prompts the user to input the text they want to summarize.
2. **Preprocessing**: The input text is tokenized into sentences using NLTK's `sent_tokenize` function. Each sentence is then processed to remove punctuation, stopwords, and perform stemming.
3. **Word Frequency**: The word frequencies in the input text are calculated using NLTK's `FreqDist` function.
4. **Sentence Scoring**: Each sentence is scored based on the sum of word frequencies of the words it contains.
5. **Summary Generation**: The top-ranked sentences are selected to form the summary. By default, it selects the top third of sentences with the highest scores.
6. **Output**: The script prints the generated summary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
