

def add_prefix_un(word):
    return "un"+ word


def make_word_groups(vocab_words):
    prefix = " :: " + vocab_words[0]
    return prefix.join(vocab_words)
  


def remove_suffix_ness(word):
    word = word[0:-4]
    if word.endswith("i"):
        word = word[0:-1] + "y"
    return word    
    

    


def adjective_to_verb(sentence, index):
    sentence = sentence[0:-1]
    
    sentence = sentence.split()
    sentence = sentence[index]+ "en"
    
    return sentence
    
  
