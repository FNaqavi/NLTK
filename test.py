# Import necessary libraries
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

print('Enter your text:')
text = input()

# Example Text (for test)
# text = """ The sun was setting on the horizon, casting a warm glow over the
# tranquil meadow. Birds chirped their final melodies of the day as they settled
# into their nests. A gentle breeze whispered through the trees, carrying with
# it the scent of wildflowers. In the distance, a river meandered lazily,
# reflecting the colors of the sky like a mirror. The air was filled with
# a sense of peace and contentment, wrapping around me like a comforting blanket.
# As darkness descended, the stars emerged one by one, painting the night sky
# with their twinkling light. It was a moment of perfect serenity."""

# Tokenization, Removing Stopwords, and Stemming
stop_words = set(stopwords.words("english"))
sentences = sent_tokenize(text)


def text_process(sentence):
    # Clean and normalize text data by removing punctuation or special characters
    sentence = re.sub(r"[^a-zA-Z0-9]", " ", sentence)

    # Tokenization
    words_in_quote = word_tokenize(sentence)

    # Remove stopwords
    filtered_words = [word for word in words_in_quote if word.casefold() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in filtered_words]

    return stemmed


# Preprocess each sentence
sentences_processes = [text_process(sentence) for sentence in sentences]

# Calculate word frequency
word_frequencies = nltk.FreqDist(word_tokenize(text))


def score_sentences(sentence, word_freq):
    sentence_score = {}

    for i, sentence in enumerate(sentence):
        score = sum(word_freq[word] for word in sentence if word in word_freq)
        sentence_score[i] = score

    return sentence_score


# Generate sentence scores
sentence_scores = score_sentences(sentences_processes, word_frequencies)

# Generate a summary by selecting top sentences
summary_sentences = []
sentence_length = len(sentences)
summary_length = int(sentence_length / 3)
if sentence_scores:
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    top_sentences = sorted_scores[:summary_length]  # Select the top 3 sentences as the summary

    for index, _ in top_sentences:
        summary_sentences.append(sentences[index])

# Join the summary sentences to create the final summary
summary = ' '.join(summary_sentences)

# Print the summary
print("\nSummary:")
print(summary)
