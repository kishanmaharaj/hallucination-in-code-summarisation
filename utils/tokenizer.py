### Custom Sentence Tokenizer

import string
import re

import spacy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))


def is_valid_word_nltk(word, config):
    """
    Check if a word is valid based on given configurations.
    ----------
    Parameters
    ----------
    word: string
    The word to be validated.
    
    config: dict
    Configuration dictionary containing the following keys:
        - "drop_stopword" (bool): If True, stopwords will be considered invalid.
        - "drop_punct" (bool): If True, punctuation marks will be considered invalid.
    
    ----------
    Returns
    -------
    bool
        True if the word is valid according to the configurations, False otherwise.
    """
    # check if word is not white space
    drop_stop = config["drop_stopword"]
    drop_punct = config["drop_punct"]

    length_acceptable = False
    stop_acceptable = False
    punct_acceptable = False

    if len(word.strip()):
        length_acceptable = True
        
        if drop_punct:
            if not word in string.punctuation:
                punct_acceptable = True
        else:
            punct_acceptable = True

        if drop_stop:
            if not word in stop_words:
                stop_acceptable = True
        else:
            stop_acceptable = True

    return length_acceptable and stop_acceptable and punct_acceptable


def tokenize_sentence(line, config):
    """
    Tokenize a sentence into words and validate them based on given configurations.
    ----------
    Parameters
    ----------
    line: string
    The sentence to be tokenized.
    
    config: dict
    Configuration dictionary containing the validation rules for words:
        - "drop_stopword" (bool): If True, stopwords will be excluded.
        - "drop_punct" (bool): If True, punctuation marks will be excluded.
    
    ----------
    Returns
    -------
    list of strings
        A list of valid words from the tokenized sentence.
    """
    words = [word.strip() for word in word_tokenize(line) if is_valid_word_nltk(word, config)]
    return words


def base_tokenize(text, config):
    """
    Tokenize text into sentences and words, and validate words based on given configurations.
    ----------
    Parameters
    ----------
    text: string
    The text to be tokenized.
    
    config: dict
    Configuration dictionary containing the validation rules for words:
        - "drop_stopword" (bool): If True, stopwords will be excluded.
        - "drop_punct" (bool): If True, punctuation marks will be excluded.
    
    ----------
    Returns
    -------
    tuple of lists
        A tuple containing two lists:
        - List of sentences from the tokenized text.
        - List of lists of valid words for each sentence.
    """

    sentences = []
    words = []
    prev_line = ""
    for line in sent_tokenize(text):
        # If the current line is just a numeral (1., 2., ..), ignore it
        match_obj = re.match(pattern="^[0-9a-z]{,2}\.?$", string=line)
        if match_obj:
            prev_line = line
            continue

        # If my previous line is just a numeral (1., 2., ..), add it to my current line
        if prev_line:
            match_obj = re.match(pattern="^[0-9a-z]{,2}+\.?$", string=prev_line)
            if match_obj:
                line = f"{prev_line.strip()} {line}"
                prev_line = ""

        if line:
            sentences.append(line)
            words.append(tokenize_sentence(line, config))

    return sentences, words


def tokenize(text, config):
    """
    Tokenize text into sentences and words, handling line breaks and validation based on given configurations.
    ----------
    Parameters
    ----------
    text: string
    The text to be tokenized.
    
    config: dict
    Configuration dictionary containing the validation rules for words:
        - "drop_stopword" (bool): If True, stopwords will be excluded.
        - "drop_punct" (bool): If True, punctuation marks will be excluded.
    
    ----------
    Returns
    -------
    tuple of lists
        A tuple containing two lists:
        - List of sentences from the tokenized text.
        - List of lists of valid words for each sentence.
    """

    sentences = []
    words = []

    for line in text.split("\n"):
        if line:

            parts = [item for item in line.split('.') if item]
            if len(parts) > 1:
                split_sents, split_words = base_tokenize(line.strip(), config)
                sentences += split_sents
                words += split_words
                sentences[-1] = sentences[-1] + "\n"
            else:
                sentences.append(line + "\n")
                split_words = tokenize_sentence(line, config)
                words.append(split_words)
        else:
            sentences.append(line + "\n")
            words.append([])

    return sentences, words