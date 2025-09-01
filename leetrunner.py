def reverse_words(sentence):

    # reverse the order of words in a sentence    

    word_list = (sentence.strip()).split()[::-1]

    return " ".join(word_list)
