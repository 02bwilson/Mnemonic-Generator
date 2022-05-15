import json
import random

def generateMnemonic(word_count=12, allow_repeating=False, wordlist=None, min_length=3):
    '''
    Parameters:
        word_count: The number of words for the mnemoinic. DEFAULT = 12
        allow_repeating: Allow words to repeat.  DEFAULT = FALSE
        wordlist: Specify file to use custom wordlist. Note - You can also just add to the given wordlist. DEFAULT = None
        min_length: The minimum length of the words in the mnemoinic. DEFAULT = 3
    Returns:
        str[]: List of the mnemoinic's composition.
    '''
    return_mnemonic = list()

    # Read in the word list
    if wordlist == None:
        word_list = open('wordlist.json')
    else:
        word_list = open(wordlist)
    word_list = json.loads(word_list.read())

    # Generate the number of words requested
    for i in range(0, word_count - 1):
        # Random word in range of word list size
        word_index = getWordIndex(allow_repeating_ind = allow_repeating, word_list_ind = word_list, return_mnemonic_ind = return_mnemonic, min_length_ind = min_length)
        while word_index is None:
            word_index = getWordIndex(allow_repeating_ind = allow_repeating, word_list_ind = word_list, return_mnemonic_ind = return_mnemonic, min_length_ind = min_length)
        return_mnemonic.append(word_list[word_index])
        word_index = 0
    return return_mnemonic

def getWordIndex(allow_repeating_ind, word_list_ind, return_mnemonic_ind, min_length_ind):
    # Picks random word
    index = random.randrange(0, len(word_list_ind))
    # Checks if word is long enough
    if len(word_list_ind[index]) >= min_length_ind:
        # If word repeats and repeats not allowed, recurse
        if allow_repeating_ind == False and word_list_ind[index] in return_mnemonic_ind:
                getWordIndex(allow_repeating_ind, word_list_ind, return_mnemonic_ind, min_length_ind)
        # If all confitions met, return
        else:
            return index
    # If not long enough, recurse
    else:
        getWordIndex(allow_repeating_ind, word_list_ind, return_mnemonic_ind, min_length_ind)
    

if __name__ == "__main__":
    print(generateMnemonic(min_length=13))
    
