"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    title = title.split()
    new_title = []

    for i in range(0,len(title)):
        word = title[i]
        word = word[0].upper() + word[1:]
        new_title.append(word)
    new_title = " ".join(new_title)
    return new_title
   
    
    
    
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """

    pass


def check_sentence_ending(sentence):
    return sentence[-1] in "!.?"
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """

    pass


def clean_up_spacing(sentence):
    return sentence.strip()
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.

    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """

    pass


def replace_word_choice(sentence, old_word, new_word):
    sentence_1 = sentence 
    sentence = sentence[0:-1]
    sentence = sentence.split()
    i = 0 
    if old_word not in sentence:
        return sentence_1
    else: 
         while i < len(sentence) and old_word != sentence[i]:
              i += 1 
             
       
    sentence[i] = new_word
    sentence = " ".join(sentence)
    sentence = sentence + "."
    return sentence
   
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """

    pass

