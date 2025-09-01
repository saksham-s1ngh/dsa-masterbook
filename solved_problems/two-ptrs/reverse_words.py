def reverse_words(sentence):

    # reverse the order of words in a sentence   
    result_str = ""
    right = len(sentence) - 1
    while right > 0:
        # we start moving from the last word
        #   and use left ptr to find start of a word
        left = right
        # the inner loop moves through a word till it reaches a space
        #   thus stopping on the first found
        while left >= 0 and sentence[left] != " ":
            left -= 1

        word = sentence[left+1:right+1] # extract word

        result_str += word + " "
        
        # move right ptr to last char of the next word
        right = left - 1

    return result_str

print(reverse_words("reverse in was string this"))