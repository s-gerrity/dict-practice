"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""

# add words as keys
# add how many times key appears in list as value
# sort by asc values
# print one by one

def word_count(phrase):
    """Count words in a sentence, and print each word and its count in ascending order."""
    
    new_phrase = phrase.split(" ")
    new_phrase = sorted(new_phrase)
    result = {}
    
    for word in new_phrase:
        if_word = result.get(word, 0)
        result[word] = if_word + 1
    
    
    for key, value in result.items():
        print(f"{key}: {value}")
        
    return



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
